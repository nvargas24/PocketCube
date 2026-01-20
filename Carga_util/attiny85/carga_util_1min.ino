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
#define MEAS1 1   // ID para contador de pulsos MEAS1
#define STATE 6   // ID para estado (no usado aquí)
#define COUNT 8   // ID para segundos de ATtiny

// Comando I2C para solicitar MEAS1
#define STR_MEAS1 '1'
#define STR_COUNT '8'

// Variables globales volátiles (usadas en ISR)
volatile uint16_t pulseCount1 = 0;  // Contador de pulsos en PB3
volatile uint16_t pulseCount_1min = 0;  // Contador de pulsos acumulado cada 60 segundos
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
    
    // Incrementa contador de segundos
    secondCounter++;
    
    // Cada 60 segundos acumula pulsos
    if (secondCounter >= 60) {
      pulseCount_1min = pulseCount1;  // Asigna valor acumulado
      pulseCount1 = 0;                // Resetea para nuevo conteo
      secondCounter = 0;
    }
  }
  
  // Verifica si el master I2C envió datos
  if (TinyWireS.available()) {
    delay(10);
    receivedChar = TinyWireS.receive();   
    
    if (receivedChar == STR_MEAS1) {
      formatSendCmd(dataRequest, MEAS1, pulseCount_1min);
      sendDataMaster(dataRequest);
    } 
    /*if (receivedChar == STR_COUNT) {
      formatSendCmd(dataRequest, COUNT, secondCounter);
      sendDataMaster(dataRequest);
    } */
    
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
    delay(100); // Delay entre envíos para estabilidad
  }
}

// Función para formatear el comando de respuesta
// Formato: "ID,valor" (ej: "1,42")
void formatSendCmd(char* buf, int id, uint16_t data)
{
  snprintf(buf, MAX_BUF_I2C, "%d,%u", id, data);
}
