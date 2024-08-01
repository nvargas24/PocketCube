/********  Librerias  ******/
#include <RadioLib.h>
#include "settings.h"
#include <EEPROM.h>
#include <virtuabotixRTC.h>
#include <Vcc.h>

/************  Variables globales  ***********/
const float VccMin = 3.0;                 // Minimum expected Vcc level, in Volts.
const float VccMax = 4.15;                // Maximum expected Vcc level, in Volts.
const float VccCorrection = 4.00 / 4.12;  // Measured Vcc by multimeter divided by reported Vcc
//long interval = 60000;
int state;
volatile bool receivedFlag = false; // flag to indicate that a packet was received
volatile bool enableInterrupt = true; // disable interrupt when it's not needed

int battVolts;
int t_cpu;
int _RSC;
int _status = 0;
int CTx;
byte _FR;

char txbuffer[80];
char superbuffer[80];

String callsign = "FOSSASAT-1";

float lastRSSI = 0.0;
float lastSNR = 0.0;

int flag1 = 0;

uint8_t uplinked[64];
uint8_t downlink[64];
uint8_t downlinklen = 0;

Vcc vcc(VccCorrection);

char cadenaTemporal[7];
char cadenaTemporal_1[7];
char cadenaTemporal_2[7];
char cadenaTemporal_3[7];

int periodo = 5000;
unsigned long TiempoAhora = 0;

/*********  Objetos globales  *********/
SX1278 radio = new Module(10, 2, 9, 3);  // Creo objeto para nuevo modulo Lora
/* SX1278 has the following connections:
   NSS pin:   10
   DIO0 pin:  2
   RESET pin: 9
   DIO1 pin:  3
*/
//SX1278 radio = new Module(10, 2, 9, 3);

virtuabotixRTC myRTC(8, 7, 6); // Creo objeto para manejo RTC


void setup() {
  Serial.begin(9600);

  Serial.println('\n');
  Serial.print("Sketch=");
  Serial.println(__FILE__);
  Serial.println('\n');

  myRTC.setDS1302Time(00, 00, 00, 6, 01, 01, 2020);

  if (MCUSR & _BV(EXTRF)) {
    // Reset button or otherwise some software reset
    // Serial.println("Reset button was pressed.");
    _RSC = EEPROM.read(7);
    _RSC = _RSC + 1;

    EEPROM.write(7, _RSC);

    // Serial.print("RST = ");
    // Serial.println(_RSC);

    MCUSR = 0;

    if (EEPROM.read(20) == 1) {
      bitWrite(_status, 4, 1);
    }

    if (EEPROM.read(16) == 1) {
      bitWrite(_status, 1, 1);

      _FR = EEPROM.read(16);
    }
  }

  if (MCUSR & (_BV(BORF) | _BV(PORF))) {
    // Brownout or Power On
    // Serial.println("Power loss occured!");
    _RSC = 0;

    EEPROM.write(2, 0);
    EEPROM.write(7, 0);
    EEPROM.write(9, 0);   //ACTIVA BALIZA CW
    EEPROM.write(11, 0);  //LOG ROBOT LISTO

    EEPROM.write(16, 0);
    EEPROM.write(20, 0);  //LOGGER VACIO


    bitWrite(_status, 0, 0);
    bitWrite(_status, 1, 0);
    bitWrite(_status, 2, 0);
    bitWrite(_status, 3, 0);
    bitWrite(_status, 4, 0);
    bitWrite(_status, 5, 0);
    bitWrite(_status, 6, 0);
    bitWrite(_status, 7, 0);

    MCUSR = 0;

    bitWrite(_status, 5, 1);
  }
}

void loop() {
  myRTC.updateTime();
  // int txt = radio.getTempRaw ();

  char InternalTemp[10];
  char BattVoltage[10];

  dtostrf(vcc.Read_Volts(), 4, 2, BattVoltage);
  dtostrf(GetTemp(), 3, 1, InternalTemp);
  analogReference(INTERNAL);
  delay(10);

  for (int lap = 0; lap <= 2; lap = lap + 1) {

    CTx = (analogRead(A2) / 8) - 7;  //CORRIENTE QUE CONSUME EL TRANSMISOR SIN MPPT menos lo que consume el led del opto -7 mA
    CTx = constrain(CTx, 0, 150);
    delay(10);
  }AfskSetup

  sprintf(txbuffer, "LW2DTZ %02d%02d%02d %sV %sC %dmA %d", myRTC.hours, myRTC.minutes, myRTC.seconds, BattVoltage, InternalTemp, CTx, _RSC);
  sprintf(superbuffer, "%s\n", txbuffer);
  delay(1000);

  setuprx();

  //SetRx();

  TiempoAhora = millis();

  // Serial.print(F("Starting to listen ... "));

  while (millis() < TiempoAhora + periodo) {
    // DIGI();
    // Rxloop();
    looprx();
  }

  // sendPACKET();
  delay(1000);
  sendLoRa();

  delay(2000);
  AfskSetup();

  delay(1000);
  AfskSetup();

  delay(1000);
  memset(superbuffer, 0, sizeof(superbuffer));

  //radio.standby();
  radio.sleep();
}
