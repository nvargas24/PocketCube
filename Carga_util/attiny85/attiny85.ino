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

// Comando I2C para solicitar MEAS1
#define STR_MEAS1 '1'

// Variables globales volátiles (usadas en ISR)
volatile uint16_t pulseCount1 = 0;  // Contador de pulsos en PB3
volatile char receivedChar = '\0';  // Carácter recibido por I2C
volatile bool lastState1 = LOW;     // Estado anterior del pin PB3 para detectar flancos

// Prototipos de funciones
void formatSendCmd(char*, int, uint16_t);

void setup() {
  // Inicializa I2C como esclavo en la dirección especificada
  TinyWireS.begin(ADDR_SLAVE_I2C);
  
  // Configura PB3 como entrada para detectar pulsos
  pinMode(PIN_MEAS1, INPUT);
  
  // Configura interrupciones PCINT para PB3
  // ATtiny85 no tiene ISR de hardware como Arduino UNO, usa PCINT (cambio de estado)
  GIMSK |= (1 << PCIE);      // Habilita interrupciones por cambio de pin (PCIE)
  PCMSK |= (1 << PIN_MEAS1); // Habilita PCINT3 para PB3
  
  // Habilita interrupciones globales
  sei();
}

void loop() {
  char dataRequest[MAX_BUF_I2C] = "\0";
  
  // Verifica si el master I2C envió datos
  if (TinyWireS.available()) {
    // Pequeño delay para estabilidad
    delay(100);
    
    // Recibe el carácter enviado por el master
    // ******* IMPORTANTE ******* // Recibe el comando I2C para saber cantidad de pulsos
    receivedChar = TinyWireS.receive();   
    
    // Si el master solicita MEAS1 ('1'), envía el contador de pulsos
    if (receivedChar == STR_MEAS1) {
      // Formatea la respuesta: "ID,valor" (ej: "1,42")
      formatSendCmd(dataRequest, MEAS1, pulseCount1);
      
      // Envía la respuesta al master
      sendDataMaster(dataRequest);
      
      // Reinicia el contador después de enviar (lectura destructiva)
      pulseCount1 = 0;
    } 
  }
}

// ISR para interrupciones PCINT (cambio de estado en pines)
// Se ejecuta cuando hay cambio en PB3 (PCINT3)
ISR(PCINT0_vect) {
  // Lee el estado actual del pin PB3
  bool currentState1 = bit_is_set(PINB, PIN_MEAS1);

  // Detecta flanco ascendente (LOW a HIGH) para contar pulso
  // PCINT detecta cualquier cambio, pero solo contamos rising edge
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
