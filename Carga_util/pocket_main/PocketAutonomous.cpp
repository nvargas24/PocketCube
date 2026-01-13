/**
 * @file PocketAutonomous.cpp
 * @brief Módulo autónomo de adquisición de datos PocketCube
 * @details No depende de aplicación externa - funciona automáticamente
 * @author Grupo SyCE - PocketCube
 */

#include "PocketAutonomous.h"

/*********** Variables privadas del módulo ***********/
static char lastDataMeas1[MAX_DATA_I2C] = "";
static char lastDataState[MAX_DATA_I2C] = "";
static char dataRequest[MAX_DATA_I2C] = "";

static bool running = false;
static bool connected = false;
static bool readNowFlag = false;
static bool newDataAvailable = false;

static uint8_t readInterval = 1;  // Intervalo en segundos (default 1s)
static uint16_t timerCompare = 15624;  // Valor para 1 segundo a 16 MHz

// Callback para nuevos datos
static void (*dataCallback)(int, const char*) = nullptr;

/****** Declaración de funciones internas *******/
static void filterValue(char *str);
static void sendToSlaveC(char c);
static int requestFromSlave();
static void configTimer(uint8_t seconds);
static void checkConnection();

/****************** Timer ISR ******************/
ISR(TIMER1_COMPA_vect) 
{
  if(running){
    readNowFlag = true;  // Señal para leer en el main loop
  }
}

/****** Función auxiliar para calcular timer *****/
/**
 * @brief Calcula el valor OCR1A basado en segundos deseados
 * @param seconds Segundos deseados
 * @return Valor de comparación para OCR1A
 */
static uint16_t calculateTimerValue(uint8_t seconds)
{
  // Formula: OCR1A = (Freq / Prescaler) * Segundos - 1
  // Para 16MHz, prescaler 1024, 1 segundo = 15624
  // Por lo tanto: 15624 * segundos
  return (15624UL * seconds) - 1;
}

/****************** Inicialización ***************/
void pocketAutoInit() 
{
  // Serial debe estar inicializado por el sketch principal
  // Wire debe estar inicializado por el sketch principal
  
  // Inicializar variables
  running = false;
  connected = false;
  readNowFlag = false;
  newDataAvailable = false;
  readInterval = 1;
  
  // Verificar conexión con esclavo
  checkConnection();
  
  // Configurar timer
  configTimer(readInterval);
  
  // Iniciar adquisición automáticamente
  pocketAutoStart();
}

/**************** Update (Loop) *****************/
void pocketAutoUpdate() 
{
  // Si debe hacer lectura (por timer o por comando manual)
  if(readNowFlag || running){
    readNowFlag = false;  // Limpiar flag
    
    // Solicitar lectura de sensor 1
    sendToSlaveC(STR_MEAS1);
    delayMicroseconds(100);  // Pequeño delay para respuesta
    
    int sizeRta = requestFromSlave();
    
    if(sizeRta > 0){
      connected = true;
      newDataAvailable = true;
      
      // Guardar último dato
      strcpy(lastDataMeas1, dataRequest);
      filterValue(lastDataMeas1);
      
      // Ejecutar callback si está definido
      if(dataCallback != nullptr){
        dataCallback(SENSOR_MEAS1, lastDataMeas1);
      }
    }
    else{
      connected = false;
    }
  }
}

/*********** Funciones públicas *************/

void pocketAutoStart()
{
  running = true;
  readNowFlag = true;  // Hacer lectura inmediata
}

void pocketAutoStop()
{
  running = false;
  readNowFlag = false;
}

bool pocketAutoIsRunning()
{
  return running;
}

bool pocketAutoSetInterval(uint8_t seconds)
{
  // Validar rango (1 a 255 segundos)
  if(seconds < 1 || seconds > 255){
    return false;
  }
  
  readInterval = seconds;
  
  // Reconfigurar el timer si está ejecutándose
  if(running){
    pocketAutoStop();
    configTimer(seconds);
    pocketAutoStart();
  }
  else{
    configTimer(seconds);
  }
  
  return true;
}

uint8_t pocketAutoGetInterval()
{
  return readInterval;
}

int pocketAutoGetLastReading(uint8_t sensorId, char* buffer, int bufferSize)
{
  const char* source = nullptr;
  
  if(sensorId == SENSOR_MEAS1){
    source = lastDataMeas1;
  }
  else if(sensorId == SENSOR_STATE){
    source = lastDataState;
  }
  else{
    return 0;
  }
  
  if(strlen(source) == 0){
    return 0;
  }
  
  // Copiar dato al buffer
  int copySize = strlen(source);
  if(copySize >= bufferSize){
    copySize = bufferSize - 1;
  }
  
  strncpy(buffer, source, copySize);
  buffer[copySize] = '\0';
  
  return copySize;
}

void pocketAutoSetDataCallback(void (*callback)(int, const char*))
{
  dataCallback = callback;
}

void pocketAutoReadNow()
{
  readNowFlag = true;
}

bool pocketAutoIsConnected()
{
  return connected;
}

void pocketAutoResetConnection()
{
  Wire.end();
  delay(100);
  Wire.begin();
  delay(100);
  checkConnection();
}

/*********** Funciones internas *************/

static void filterValue(char *str)
{
  // Encuentra y elimina todo antes de la coma
  char *commaPtr = strchr(str, ',');
  
  if (commaPtr != nullptr) {
    int offset = commaPtr - str;
    strcpy(str, commaPtr + 1);
  }
}

static void sendToSlaveC(char c)
{
  Wire.beginTransmission(I2C_SLAVE_ADDR);
  Wire.write(c);
  Wire.endTransmission();
}

static int requestFromSlave()
{
  uint8_t index = 0;  
  char receivedChar;
  int size_rta = 0;

  Wire.requestFrom(I2C_SLAVE_ADDR, (uint8_t)MAX_DATA_I2C);

  while (Wire.available() && (index < MAX_DATA_I2C)) {
    receivedChar = Wire.read();
    // Solo caracteres imprimibles ASCII (32-126)
    if (receivedChar >= 32 && receivedChar <= 126) {
      dataRequest[index] = receivedChar;
      index++;
    } 
    else {
      break;
    }
  }
  dataRequest[index] = '\0';

  size_rta = strlen(dataRequest);

  return size_rta;
}

static void configTimer(uint8_t seconds)
{
  // Calcular valor de comparación
  timerCompare = calculateTimerValue(seconds);
  
  noInterrupts();
  
  // Detener timer
  TCCR1A = 0;
  TCCR1B = 0;
  TCNT1 = 0;
  
  // Configurar nuevo valor de comparación
  OCR1A = timerCompare;
  
  // Modo CTC (Clear Timer on Compare Match)
  TCCR1B |= (1 << WGM12);
  
  // Prescaler 1024
  TCCR1B |= (1 << CS12) | (1 << CS10);
  
  // Habilitar interrupción
  TIMSK1 |= (1 << OCIE1A);
  
  interrupts();
}

static void checkConnection()
{
  // Intenta comunicarse con el esclavo
  Wire.beginTransmission(I2C_SLAVE_ADDR);
  int error = Wire.endTransmission();
  
  connected = (error == 0);
}
