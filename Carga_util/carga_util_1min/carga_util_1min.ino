/**
 * @file attiny85.ino
 * @brief Código para ATtiny85 como carga útil en PocketCube
 * @details Cuenta pulsos en PB3 usando PCINT y responde a solicitudes I2C del Pocket Main
 * @author Grupo SyCE - PocketCube
 */

#include <avr/interrupt.h>
#include <avr/io.h>
#include <TinyWireS.h>

// Configuración I2C
#define ADDR_SLAVE_I2C 0x08  // Dirección del esclavo I2C (misma que Pocket Main)

// Pines para sensores
#define PIN_MEAS1 PB3  // Pin PB3 para detectar pulsos de MEAS1 (PCINT3)

// Buffers y constantes
#define MAX_BUF_I2C 33  // Tamaño máximo del buffer I2C

// IDs de datos (igual que en Pocket Main)
#define CPM 1   // ID para contador de pulsos acumulado en el ultimo minuto
#define CPS_NOW 2   // ID para pulsos por segundo acumulado durante ese minuto
#define TIME 3   // ID para segundos transcurridos
#define CPS_NOW_ACCUM 4   // ID para pulsos por segundo acumulado durante ese minuto

// Comando I2C recibidos
#define STR_CPM '1'
#define STR_CPS_NOW '2'
#define STR_TIME '3'
#define STR_CPS_NOW_ACUMM '4'

// Variables globales volátiles (usadas en ISR)
volatile uint16_t pulseCount1 = 0;  // Contador de pulsos en PB3
volatile uint16_t pulseCount_1min = 0;  // Contador de pulsos acumulado cada 60 segundos
volatile uint16_t previousPulseCount = 0;  // Contador anterior para calcular pulsos por segundo
volatile uint16_t currentPulses = 0;  // Pulsos en el último segundo (no acumulado)
volatile char receivedChar = '\0';  // Carácter recibido por I2C
volatile bool lastState1 = LOW;     // Estado anterior del pin PB3 para detectar flancos
static uint16_t secondCounter = 0;

// Prototipos de funciones
void formatSendCmd(char*, int, uint16_t);

void setup() {
  // Inicializa I2C como esclavo en la dirección especificada
  TinyWireS.begin(ADDR_SLAVE_I2C);
  
  // Configura PB3 como entrada para detectar pulsos
  pinMode(PIN_MEAS1, INPUT);
  
  // Configura interrupciones PCINT para PB3
  GIMSK |= (1 << PCIE);      // Habilita interrupciones por cambio de pin (PCIE)
  PCMSK |= (1 << PIN_MEAS1); // Habilita PCINT3 para PB3
  
  // Habilita interrupciones globales
  sei();
}

void loop() {
  char dataRequest[MAX_BUF_I2C] = "\0";
  static unsigned long lastSecondTime = 0;
  unsigned long currentTime = millis();
  
  // Polling cada 1 segundo (10000 ms real en ATtiny85)
  if (currentTime - lastSecondTime >= 10000) {
    lastSecondTime = currentTime;
    
    // Calcula pulsos en el último segundo
    currentPulses = pulseCount1 - previousPulseCount;
    previousPulseCount = pulseCount1;
    
    // Incrementa contador de segundos
    secondCounter++;
    
    // Cada 60 segundos acumula pulsos
    if (secondCounter >= 60) {
      pulseCount_1min = pulseCount1;  // Asigna valor acumulado
      pulseCount1 = 0;                // Resetea para nuevo conteo
      secondCounter = 0;
      previousPulseCount = 0;         // Resetea también el contador anterior
    }
  }
  
  // Verifica si el master I2C envió datos
  if (TinyWireS.available()) {
    delay(10);
    receivedChar = TinyWireS.receive();   
    
    if (receivedChar == STR_CPM) {
      formatSendCmd(dataRequest, CPM, pulseCount_1min);
      sendDataMaster(dataRequest);
    } 
    if (receivedChar == STR_CPS_NOW) {
      formatSendCmd(dataRequest, CPS_NOW, currentPulses);
      sendDataMaster(dataRequest);
    } 
    if (receivedChar == STR_TIME) {
      formatSendCmd(dataRequest, TIME, secondCounter);
      sendDataMaster(dataRequest);
    } 
    if (receivedChar == STR_CPS_NOW_ACUMM) {
      formatSendCmd(dataRequest, CPS_NOW_ACCUM, pulseCount1);
      sendDataMaster(dataRequest);
    }

  }
}

// ISR para interrupciones PCINT (cambio de estado en pines)
ISR(PCINT0_vect) {
  // Lee el estado actual del pin PB3
  bool currentState1 = bit_is_set(PINB, PIN_MEAS1);

  // Detecta flanco ascendente (LOW a HIGH) para contar pulso
  if (currentState1 && !lastState1) {
    pulseCount1++; // Incrementa el contador de pulsos
  }

  // Actualiza el estado anterior para la próxima interrupción
  lastState1 = currentState1;
}

// Función para enviar datos al master I2C
// TinyWireS.send() envía byte a byte
void sendDataMaster(char *message) {
  // Envía cada carácter del mensaje
  for (int i = 0; message[i] != '\0'; i++) {
    TinyWireS.send(message[i]);
    delay(10); // Delay entre envíos para estabilidad
  }
}

// Función para formatear el comando de respuesta
// Formato: "ID,valor" (ej: "1,42")
void formatSendCmd(char* buf, int id, uint16_t data)
{
  snprintf(buf, MAX_BUF_I2C, "%d,%u", id, data);
}
