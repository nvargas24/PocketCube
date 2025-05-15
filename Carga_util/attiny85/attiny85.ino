#include <avr/interrupt.h>
#include <avr/io.h>
#include <TinyWireS.h>

#define ADDR_SLAVE_I2C 0x08
#define PIN_MEAS1 PB3 // Usaremos PB3 para detectar pulsos (PCINT3)

#define MAX_BUF_I2C 33

#define MEAS1 1
#define STATE 6

#define STR_MEAS1 '1'

volatile uint16_t pulseCount1 = 0;  // Contador de pulsos en PB3
volatile char receivedChar = '\0'; // Carácter recibido por I2C
volatile bool lastState1 = LOW;     // Estado anterior del pin PB3

void formatSendCmd(char*, int, uint16_t);

void setup() {
  TinyWireS.begin(ADDR_SLAVE_I2C);
  pinMode(PIN_MEAS1, INPUT); // Configura el pin PB3 como entrada
  
  // Configura las interrupciones de cambio de estado en PB3 (PCINT3)
  GIMSK |= (1 << PCIE);      // Habilita las interrupciones por cambio de pin
  PCMSK |= (1 << PIN_MEAS1);  // Habilita la interrupción en el pin PB3
  
  sei(); // Habilita interrupciones globales
}

void loop() {
  char dataRequest[MAX_BUF_I2C] = "\0";
  // Comprueba si hay datos disponibles para recibir
  if (TinyWireS.available()) {
    delay(100);
    receivedChar = TinyWireS.receive(); // Recibe un carácter por I2C

    // Verifico que MEAS solicita
    if (receivedChar == STR_MEAS1) {
      formatSendCmd(dataRequest, MEAS1, pulseCount1);
      //snprintf(dataRequest, MAX_BUF_I2C, "%u", pulseCount1);
      sendDataMaster(dataRequest);
      pulseCount1 = 0; // Reinicia el contador después de enviar los datos
    } 
  }
}

// Manejador de interrupción para contar los pulsos en PB3 (PCINT3) y PB4 (PCINT4)
ISR(PCINT0_vect) {
  // Lee el estado actual del pin PB3
  bool currentState1 = bit_is_set(PINB, PIN_MEAS1);

  // Detecta flanco ascendente en PB3
  if (currentState1 && !lastState1) {
    pulseCount1++; // Incrementa el contador de pulsos en flanco ascendente
  }

  // Actualiza el estado anterior
  lastState1 = currentState1;
}

void sendDataMaster(char *message) {
  // Enviar el mensaje carácter por carácter
  for (int i = 0; message[i] != '\0'; i++) {
    TinyWireS.send(message[i]); // Envía cada carácter del mensaje
    delay(100); // Retraso entre envíos
  }
}

void formatSendCmd(char* buf, int id, uint16_t data)
{
  snprintf(buf, MAX_BUF_I2C, "%d,%u", id, data);
}
