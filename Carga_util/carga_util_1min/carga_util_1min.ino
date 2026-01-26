/**
 * @file attiny85.ino
 * @brief Código para ATtiny85 como carga útil en PocketCube
 * @details Cuenta pulsos en PB3 usando PCINT y responde a solicitudes I2C del Pocket Main
 *          El conteo de tiempo se realiza con TIMER0 (sin millis)
 * @author Grupo SyCE - PocketCube
 */

#include <avr/interrupt.h>
#include <avr/io.h>
#include <TinyWireS.h>

/* =========================
   Configuración I2C
   ========================= */
#define ADDR_SLAVE_I2C 0x08

/* =========================
   Pines
   ========================= */
#define PIN_MEAS1 PB3   // PCINT3

/* =========================
   Buffers
   ========================= */
#define MAX_BUF_I2C 33

/* =========================
   IDs de datos
   ========================= */
#define CPM            1
#define CPS_NOW        2
#define TIME           3
#define CPS_NOW_ACCUM  4
#define CPS_TIME       5
#define CPM_TIME       6

/* =========================
   Comandos I2C
   ========================= */
#define STR_CPM             '1'
#define STR_CPS_NOW         '2'
#define STR_TIME            '3'
#define STR_CPS_NOW_ACUMM   '4'
#define STR_CPS_TIME        '5'
#define STR_CPM_TIME        '6'

/* =========================
   Variables globales
   ========================= */
volatile uint16_t pulseCount1 = 0;
volatile uint16_t pulseCount_1min = 0;
volatile uint16_t previousPulseCount = 0;
volatile uint16_t currentPulses = 0;

volatile bool lastState1 = LOW;
volatile char receivedChar = '\0';

/* ---- Tiempo por TIMER ---- */
volatile uint16_t msCounter = 0;
volatile bool oneSecondFlag = false;
static uint16_t secondCounter = 0;

/* =========================
   Prototipos
   ========================= */
void setupTimer0_1s(void);
void sendDataMaster(char *message);
void formatSendCmd(char* buf, int id, uint16_t data);
void formatSendCmdLong(char* buf, int id, uint16_t data, uint16_t data2);

/* =========================
   SETUP
   ========================= */
void setup() {
  TinyWireS.begin(ADDR_SLAVE_I2C);

  pinMode(PIN_MEAS1, INPUT);

  /* --- PCINT PB3 --- */
  GIMSK |= (1 << PCIE);
  PCMSK |= (1 << PIN_MEAS1);

  setupTimer0_1s();

  sei();
}

/* =========================
   LOOP
   ========================= */
void loop() {
  char dataRequest[MAX_BUF_I2C] = "\0";

  /* ---- Evento de 1 segundo ---- */
  if (oneSecondFlag) {
    oneSecondFlag = false;

    currentPulses = pulseCount1 - previousPulseCount;
    previousPulseCount = pulseCount1;

    secondCounter++;

    if (secondCounter >= 60) {
      pulseCount_1min = pulseCount1;
      pulseCount1 = 0;
      previousPulseCount = 0;
      secondCounter = 0;
    }
  }

  /* ---- Recepción I2C ---- */
  if (TinyWireS.available()) {
    receivedChar = TinyWireS.receive();

    switch (receivedChar) {
      case STR_CPM:
        formatSendCmd(dataRequest, CPM, pulseCount_1min);
        break;

      case STR_CPS_NOW:
        formatSendCmd(dataRequest, CPS_NOW, currentPulses);
        break;

      case STR_TIME:
        formatSendCmd(dataRequest, TIME, secondCounter);
        break;

      case STR_CPS_NOW_ACUMM:
        formatSendCmd(dataRequest, CPS_NOW_ACCUM, pulseCount1);
        break;

      case STR_CPS_TIME:
        formatSendCmdLong(dataRequest, CPS_TIME, currentPulses, secondCounter);
        break;

      case STR_CPM_TIME:
        formatSendCmdLong(dataRequest, CPM_TIME, pulseCount_1min, secondCounter);
        break;

      default:
        return;
    }

    sendDataMaster(dataRequest);
  }
}

/* =========================
   ISR PCINT – Pulsos
   ========================= */
ISR(PCINT0_vect) {
  bool currentState1 = bit_is_set(PINB, PIN_MEAS1);

  if (currentState1 && !lastState1) {
    pulseCount1++;
  }

  lastState1 = currentState1;
}

/* =========================
   ISR TIMER0 – 1 ms
   ========================= */
ISR(TIMER0_COMPA_vect) {
  msCounter++;

  if (msCounter >= 1000) {
    msCounter = 0;
    oneSecondFlag = true;
  }
}

/* =========================
   Configuración TIMER0
   ========================= */
void setupTimer0_1s(void) {
  cli();

  TCCR0A = (1 << WGM01);                   // CTC
  TCCR0B = (1 << CS01) | (1 << CS00);      // Prescaler 64

  /* ATtiny85 @ 8MHz:
     8MHz / 64 = 125kHz
     125kHz / 125 = 1kHz -> 1ms
  */
  OCR0A = 124;

  TIMSK |= (1 << OCIE0A);

  sei();
}

/* =========================
   Envío I2C
   ========================= */
void sendDataMaster(char *message) {
  for (uint8_t i = 0; message[i] != '\0'; i++) {
    TinyWireS.send(message[i]);
  }
}

/* =========================
   Formateo de mensajes
   ========================= */
void formatSendCmd(char* buf, int id, uint16_t data) {
  snprintf(buf, MAX_BUF_I2C, "%d,%u", id, data);
}

void formatSendCmdLong(char* buf, int id, uint16_t data, uint16_t data2) {
  snprintf(buf, MAX_BUF_I2C, "%d,%u %u", id, data, data2);
}
