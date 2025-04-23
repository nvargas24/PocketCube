#include <TimeLib.h>
#include "SoftDS3231RTC.h"

void setup() {
  Serial.begin(9600);
  while (!Serial); // wait for serial port to connect. Needed for native USB

  Serial.println(F("Configuracion RTC INIT"));
  /* Verifico deteccion de RTC */
  while (!RTC.begin()) {
    Serial.println(F("NO SE ENCUENTRA RTC"));
    delay(1000); // Añadir un pequeño retraso para evitar el bucle rápido
  }

  /* Fijo datetime en caso de desconexion de la alimentacion */
  if (RTC.lostPower()) {
    tmElements_t tm;
    breakTime(now(), tm); // Fijar a fecha y hora de compilacion
    RTC.adjust(tm);
    // tm.Year = CalendarYrToTm(2024);
    // tm.Month = 9;
    // tm.Day = 15;
    // tm.Hour = 21;
    // tm.Minute = 12;
    // tm.Second = 0;
    // RTC.adjust(tm); // Fijar a fecha y hora específica. En el ejemplo, 15 de Septiembre de 2024 a las 21:12:00
  }

  setSyncProvider(RTC.get);   // the function to get the time from the RTC
  if (timeStatus() != timeSet) {
    Serial.println("Unable to sync with the RTC");
  } else {
    Serial.println("RTC has set the system time");
  }
}

void loop() {
  if (timeStatus() == timeSet) {
    digitalClockDisplay();
  } else {
    Serial.println("The time has not been set. Please run the TimeRTCSet example.");
    delay(4000);
  }
  delay(1000);
}

void digitalClockDisplay() {
  // digital clock display of the time
  Serial.print(hour());
  printDigits(minute());
  printDigits(second());
  Serial.print(" - ");
  Serial.print(day());
  Serial.print("/");
  Serial.print(month());
  Serial.print("/");
  Serial.print(year());
  Serial.println();
}

void printDigits(int digits) {
  // utility function for digital clock display: prints preceding colon and leading 0
  Serial.print(":");
  if (digits < 10)
    Serial.print('0');
  Serial.print(digits);
}