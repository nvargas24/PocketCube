/* Copyright 2024, UTN-FRH
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 * 1. Redistributions of source code must retain the above copyright notice,
 *    this list of conditions and the following disclaimer.
 *
 * 2. Redistributions in binary form must reproduce the above copyright notice,
 *    this list of conditions and the following disclaimer in the documentation
 *    and/or other materials provided with the distribution.
 *
 * 3. Neither the name of the copyright holder nor the names of its
 *    contributors may be used to endorse or promote products derived from this
 *    software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 *
 */

/**
 * @author Grupo SyCE - PocketCube
 * @authors Ing. Vargas Nahuel 
 * @authors Vargas Santiago
 */

/****** Encabezados *****/
#include <SPI.h>
#include "RTClib.h"

/****************** Variables globales ***************/ 
/*------------------- RTC --------------------*/
// Creo objeto RTC_DS1307 rtc;
RTC_DS3231 rtc;

/*----- Comunicacion master-slave I2C ------*/
const int SS_PIN = 2; //   ver para ESP32 38 PINES
char response[33];

/********* Declaracion de funciones internas *********/
void printDate();
void configInitialRTC();
void sendToSlave(String );
String datetime2str(DateTime date);
void requestFromSlave();

/****************** Funciones Arduino ****************/
/**
 * @brief Configuracion inicial
 * @return nothing
 */
void setup() 
{
  Serial.begin(115200); // Frecuencia en baudios para serial
  SPI.begin();
  pinMode(SS_PIN, OUTPUT);
  delay(1000); 
  configInitialRTC();
}

/**
 * @brief Bucle de ejecucion de programa principal
 * @attention solo RTC por el momento
 * @return nothing
 */
void loop() 
{
  String datetimeStr;

  // Obtener fecha actual y mostrar por Serial
  DateTime now = rtc.now();
  //printDate(now);
  datetimeStr = datetime2str(now);
  // Enviar data a slave
  sendToSlave(datetimeStr.c_str(), sizeof(datetimeStr.c_str())-1);
  requestFromSlave();

  delay(1000);
}

/**************** Funciones internas  *****************/
/**
 * @brief Escritura por puerto serial, solo test de RTC
 * @return nothing
 */
void printDate(DateTime date)
{
  Serial.print(date.year(), DEC);
  Serial.print('-');
  Serial.print(date.month(), DEC);
  Serial.print('-');
  Serial.print(date.day(), DEC);
  Serial.print(" ");
  Serial.print(date.hour(), DEC);
  Serial.print(':');
  Serial.print(date.minute(), DEC);
  Serial.print(':');
  Serial.print(date.second(), DEC);
  Serial.println();
}

/**
 * @brief Formatear la fecha y hora como "YYYY-MM-DD HH:MM:SS"
 * @return str de fecha y hora
 */
String datetime2str(DateTime date)
{
  char datetimeStr[20];

  snprintf(datetimeStr, sizeof(datetimeStr), "%04d-%02d-%02d %02d:%02d:%02d", 
           date.year(), date.month(), date.day(), 
           date.hour(), date.minute(), date.second());

  return String(datetimeStr);
}

/**
 * @brief Verficación conexion con RTC
 * @return nothing
 */
void configInitialRTC()
{
  if (!rtc.begin()) {
    Serial.println(F("NO SE ENCUENTRA RTC"));
    while (1);
  }
  // Si se ha perdido la corriente, fijar fecha y hora
  if (rtc.lostPower()) {
    rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));// Fijar a fecha y hora de compilacion
    // rtc.adjust(DateTime(2024, 8, 3, 18, 0, 0)); // Fijar a fecha y hora específica. En el ejemplo, 3 de Enero de 2024 a las 18:00:00
  }
}

/**
 * @brief Enviar data a slave I2C
 * @return nothing
 */
void sendToSlave(const char *data, size_t length)
{
  Serial.print("Sdata to Slave: ");
  Serial.println(data);

  digitalWrite(SS_PIN, LOW); // Activa el esclavo
  
  for (size_t i = 0; i < length; i++) {
    SPI.transfer(data[i]); // Envía un byte
    delay(10); // Pequeña pausa para asegurar la sincronización
  }

  digitalWrite(SS_PIN, HIGH); // Desactiva el esclavo
}

/**
 * @brief Respuesta de Slave I2C
 * @return String con mensaje de Slave
 */
void requestFromSlave()
{
  uint8_t index = 0;  
  size_t length = sizeof(response); 

  digitalWrite(SS_PIN, LOW); // Activa el esclavo

  for (size_t i = 0; i < length; i++) {
    response[i] = SPI.transfer(0x00); // Envía dummy data (0x00) para recibir respuesta
    delay(10); // Pequeña pausa para asegurar la sincronización
  }

  digitalWrite(SS_PIN, HIGH); // Desactiva el esclavo

}
