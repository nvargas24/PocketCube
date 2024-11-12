#include <Wire.h>

#define ADDR_SLAVE_I2C 0x08
#define PIN_MEAS1 2  // Usaremos el pin digital 2 para detectar pulsos (INT0)
#define PIN_MEAS2 3  // Usaremos el pin digital 3 para detectar pulsos (INT1)

#define MAX_BUF_I2C 33

#define MEAS1 1
#define MEAS2 2
#define RTC 3
#define EEPROM_USED 4
#define EEPROM_DATA 5
#define STATE 6

#define STR_MEAS1 '1'
#define STR_MEAS2 '2'

volatile uint16_t pulseCount1 = 0;  // Contador de pulsos en PIN_MEAS1
volatile uint16_t pulseCount2 = 0;  // Contador de pulsos en PIN_MEAS2
volatile char receivedChar = '\0'; // Carácter recibido por I2C
volatile bool lastState1 = LOW;     // Estado anterior del pin PIN_MEAS1
volatile bool lastState2 = LOW;     // Estado anterior del pin PIN_MEAS2

void formatSendCmd(char*, int, uint16_t);

void setup() {
  Wire.begin(ADDR_SLAVE_I2C);
  pinMode(PIN_MEAS1, INPUT); // Configura el pin PIN_MEAS1 como entrada
  pinMode(PIN_MEAS2, INPUT); // Configura el pin PIN_MEAS2 como entrada
  
  // Configura interrupciones en los pines digitales 2 y 3
  attachInterrupt(digitalPinToInterrupt(PIN_MEAS1), countPulse1, RISING);
  attachInterrupt(digitalPinToInterrupt(PIN_MEAS2), countPulse2, RISING);

  Wire.onRequest(sendDataMaster); // Establece función de solicitud I2C
  Wire.onReceive(receiveEvent);   // Establece función de recepción I2C
}

void loop() {
  // No se requiere hacer nada en el loop
}

void countPulse1() {
  pulseCount1++; // Incrementa el contador de pulsos para PIN_MEAS1
}

void countPulse2() {
  pulseCount2++; // Incrementa el contador de pulsos para PIN_MEAS2
}

// Función de solicitud de datos desde el maestro I2C
void sendDataMaster() {
  char dataRequest[MAX_BUF_I2C] = "\0";

  if (receivedChar == STR_MEAS2) {
    formatSendCmd(dataRequest, MEAS2, pulseCount2);
    pulseCount2 = 0; // Reinicia el contador después de enviar los datos
  } else if (receivedChar == STR_MEAS1) {
    formatSendCmd(dataRequest, MEAS1, pulseCount1);
    pulseCount1 = 0; // Reinicia el contador después de enviar los datos
  }

  // Enviar el mensaje carácter por carácter
  for (int i = 0; dataRequest[i] != '\0'; i++) {
    Wire.write(dataRequest[i]); // Envía cada carácter del mensaje
  }
}

// Función de recepción de datos desde el maestro I2C
void receiveEvent(int numBytes) {
  if (Wire.available()) {
    receivedChar = Wire.read(); // Recibe un carácter por I2C
  }
}

void formatSendCmd(char* buf, int id, uint16_t data) {
  snprintf(buf, MAX_BUF_I2C, "%d,%u", id, data);
}
