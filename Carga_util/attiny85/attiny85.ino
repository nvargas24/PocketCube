#include <avr/interrupt.h>
#include <avr/io.h>
#include <TinyWireS.h>

#define ADDR_SLAVE_I2C 0x08
#define PIN_MEAS1 PB3 // Usaremos PB3 para detectar pulsos (PCINT3)
#define PIN_MEAS2 PB4 // Usaremos PB4 para detectar pulsos (PCINT4)

#define MAX_BUF_I2C 33

#define MEAS1 1
#define MEAS2 2
#define RTC 3
#define EEPROM_USED 4
#define EEPROM_DATA 5
#define STATE 6

#define STR_MEAS1 '1'
#define STR_MEAS2 '2'

volatile uint16_t pulseCount1 = 0;  // Contador de pulsos en PB3
volatile uint16_t pulseCount2 = 0;  // Contador de pulsos en PB4
volatile char receivedChar = '\0'; // Carácter recibido por I2C
volatile bool lastState1 = LOW;     // Estado anterior del pin PB3
volatile bool lastState2 = LOW;     // Estado anterior del pin PB4

void setup() {
  TinyWireS.begin(ADDR_SLAVE_I2C);
  pinMode(PIN_MEAS1, INPUT); // Configura el pin PB3 como entrada
  pinMode(PIN_MEAS2, INPUT); // Configura el pin PB4 como entrada
  
  // Configura las interrupciones de cambio de estado en PB3 (PCINT3) y PB4 (PCINT4)
  GIMSK |= (1 << PCIE);      // Habilita las interrupciones por cambio de pin
  PCMSK |= (1 << PIN_MEAS1);  // Habilita la interrupción en el pin PB3
  PCMSK |= (1 << PIN_MEAS2);  // Habilita la interrupción en el pin PB4
  
  sei(); // Habilita interrupciones globales
}

void loop() {
  char dataRequest[MAX_BUF_I2C] = "\0";
  // Comprueba si hay datos disponibles para recibir
  if (TinyWireS.available()) {
    receivedChar = TinyWireS.receive(); // Recibe un carácter por I2C
    
    // Verifico que MEAS solicita
    if (receivedChar == STR_MEAS2) {
      snprintf(dataRequest, MAX_BUF_I2C, "%u", pulseCount2);
      sendDataMaster(dataRequest);
      pulseCount2 = 0; // Reinicia el contador después de enviar los datos
    }
    if (receivedChar == STR_MEAS1) {
      snprintf(dataRequest, MAX_BUF_I2C, "%u", pulseCount1);
      sendDataMaster(dataRequest);
      pulseCount1 = 0; // Reinicia el contador después de enviar los datos
    } 
  }
}

// Manejador de interrupción para contar los pulsos en PB3 (PCINT3) y PB4 (PCINT4)
ISR(PCINT0_vect) {
  // Lee el estado actual del pin PB3
  bool currentState1 = bit_is_set(PINB, PIN_MEAS1);
  // Lee el estado actual del pin PB4
  bool currentState2 = bit_is_set(PINB, PIN_MEAS2);

  // Detecta flanco ascendente en PB3
  if (currentState1 && !lastState1) {
    pulseCount1++; // Incrementa el contador de pulsos en flanco ascendente
  }
  // Detecta flanco ascendente en PB4
  if (currentState2 && !lastState2) {
    pulseCount2++; // Incrementa el contador de pulsos en flanco ascendente
  }

  // Actualiza el estado anterior
  lastState1 = currentState1;
  lastState2 = currentState2;
}

void sendDataMaster(char *message) {
  // Enviar el mensaje carácter por carácter
  for (int i = 0; message[i] != '\0'; i++) {
    TinyWireS.send(message[i]); // Envía cada carácter del mensaje
    delay(100); // Retraso entre envíos
  }
}
