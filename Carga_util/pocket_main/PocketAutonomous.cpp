/**
 * @file PocketAutonomous.cpp
 * @brief Módulo simplificado de adquisición autónoma de datos PocketCube
 * @details Lecturas automáticas cada 1 segundo, sin dependencias externas
 * @author Grupo SyCE - PocketCube
 */

#include "PocketAutonomous.h"

/*********** Variables privadas del módulo ***********/
static char lastData[MAX_DATA_I2C] = "";
static char dataRequest[MAX_DATA_I2C] = "";

static bool running = false;
static bool connected = false;
static bool readNowFlag = false;

/****** Declaración de funciones internas *******/
static void sendToSlaveC(char c);
static int requestFromSlave();
static void configTimer();
static void checkConnection();

/****************** Timer ISR ******************/
ISR(TIMER1_COMPA_vect) 
{
  if(running){
    readNowFlag = true;
  }
}

/****************** Inicialización ***************/
void pocketAutoInit() 
{
  // Wire debe estar inicializado por el sketch principal
  
  // Inicializar variables
  running = false;
  connected = false;
  readNowFlag = false;
  
  // Verificar conexión con esclavo
  checkConnection();
  
  // Configurar timer a 1 segundo
  configTimer();
}

/**************** Update (Loop) *****************/
void pocketAutoUpdate() 
{
  if(readNowFlag){
    readNowFlag = false;
    
    // Solicitar lectura de sensor 1
    sendToSlaveC(STR_MEAS1);
    delayMicroseconds(100);
    
    int sizeRta = requestFromSlave();
    
    if(sizeRta > 0){
      connected = true;
      
      // Guardar último dato (filtrar valor después de coma)
      strcpy(lastData, dataRequest);
      char *commaPtr = strchr(lastData, ',');
      if (commaPtr != nullptr) {
        strcpy(lastData, commaPtr + 1);
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
  readNowFlag = true;  // Lectura inmediata
}

void pocketAutoStop()
{
  running = false;
  readNowFlag = false;
}

int pocketAutoGetData(char* buffer, int bufferSize)
{
  if(strlen(lastData) == 0){
    return 0;
  }
  
  int copySize = strlen(lastData);
  if(copySize >= bufferSize){
    copySize = bufferSize - 1;
  }
  
  strncpy(buffer, lastData, copySize);
  buffer[copySize] = '\0';
  
  return copySize;
}

bool pocketAutoIsConnected()
{
  return connected;
}

/*********** Funciones internas *************/

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

static void configTimer()
{
  noInterrupts();
  
  TCCR1A = 0;
  TCCR1B = 0;
  TCNT1 = 0;
  
  OCR1A = 15624;  // 1 segundo a 16MHz con prescaler 1024
  
  TCCR1B |= (1 << WGM12);
  TCCR1B |= (1 << CS12) | (1 << CS10);
  
  TIMSK1 |= (1 << OCIE1A);
  
  interrupts();
}

static void checkConnection()
{
  Wire.beginTransmission(I2C_SLAVE_ADDR);
  int error = Wire.endTransmission();
  
  connected = (error == 0);
}
