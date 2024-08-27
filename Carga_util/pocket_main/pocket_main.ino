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
#include <Wire.h>
#include "RTClib.h"

/*********************** Macros ******************8***/
#define MAX_DATA_I2C 33

/****************** Variables globales ***************/ 
/* RTC */
RTC_DS3231 rtc; // Creo objeto RTC_DS1307 rtc;
String datetimeStr;  //

/* I2C */
const byte I2C_SLAVE_ADDR = 0x20; // Direccion I2C de Slave
char dataRequest[MAX_DATA_I2C]; // Str respuesta de Slave
char dataSend[MAX_DATA_I2C]; // Str a enviar de Master

/********* Declaracion de funciones internas *********/
/* RTC */
void printDate();
void configInitialRTC();
String datetime2str(DateTime date);

/* I2C */
void sendToSlave(String );
void requestFromSlave();

/****************** Funciones Arduino ****************/
/**
 * @brief Configuracion inicial
 * @return nothing
 */
void setup() 
{
  Serial.begin(115200); // Frecuencia en baudios para serial
  Wire.begin(); // Inicializo comunicacion I2C
  delay(1000); 
  configInitialRTC(); // Inicializo configuiracion de RTC
}

/**
 * @brief Bucle de ejecucion de programa principal
 * @attention solo RTC por el momento
 * @return nothing
 */
void loop() 
{
  DateTime now = rtc.now(); // Obtener fecha de RTC

  /* I2C */
  datetimeStr = datetime2str(now); // Conversion de datetime a Str
  snprintf(dataSend, datetimeStr.length()+1, "%s", datetimeStr.c_str()); // Conversion a array
  sendToSlave(dataSend); // Enviar data a slave
  requestFromSlave(); // Respuesta de slave

  /* Serial */
  // Identificacion por comando en formato CSV
  // * Valor para DAC:ID,value -> 1,1.23 
  // ** ID: 1->Meas1, 2->Meas2, 3->RTC


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
  /* Verifico deteccion de RTC */
  if (!rtc.begin()){
    Serial.println(F("NO SE ENCUENTRA RTC"));
    while (1);
  }
  
  /* Fijo datetime en caso de desconexion de la alimentacion */
  if (rtc.lostPower()){
    rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));// Fijar a fecha y hora de compilacion
    // rtc.adjust(DateTime(2024, 8, 3, 18, 0, 0)); // Fijar a fecha y hora específica. En el ejemplo, 3 de Enero de 2024 a las 18:00:00
  }
}

/**
 * @brief Enviar data a slave I2C
 * @return nothing
 */
void sendToSlave(const char *data)
{
  /* Verificacion de datos a enviar */
  Serial.print("S-Slave: ");
  Serial.println(data);

  /* Envio datos I2C */
  Wire.beginTransmission(I2C_SLAVE_ADDR);
  Wire.write((const uint8_t *)data, strlen(data));
  Wire.endTransmission();
}

/**
 * @brief Respuesta de Slave I2C
 * @return String con mensaje de Slave
 */
void requestFromSlave()
{
  uint8_t index = 0;  
  
  /* Preparo Master para recibir respuesta de Slave  */
  Wire.requestFrom(I2C_SLAVE_ADDR, sizeof(dataRequest)); // Solicitud a slave

  while (Wire.available() && index < sizeof(dataRequest) - 1) {
    dataRequest[index++] = Wire.read();
  }
  dataRequest[index] = '\0'; // Terminar el string

  /* Verifico datos recibidos */
  Serial.print("R-Slave: ");
  Serial.println(dataRequest);
}