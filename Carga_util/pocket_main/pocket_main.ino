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

/****************** Variables globales ***************/ 
/*------------------- RTC --------------------*/
// Creo objeto RTC_DS1307 rtc;
RTC_DS3231 rtc;

/* String para identificar dia de la semana */
String daysOfTheWeek[7] = { 
  "Domingo", 
  "Lunes", 
  "Martes", 
  "Miercoles", 
  "Jueves", 
  "Viernes", 
  "Sabado" 
};

/* String para identificar mes */
String monthsNames[12] = { 
  "Enero", 
  "Febrero", 
  "Marzo", 
  "Abril", 
  "Mayo",  
  "Junio", 
  "Julio",
  "Agosto",
  "Septiembre",
  "Octubre",
  "Noviembre",
  "Diciembre" 
};

/*----- Comunicacion master-slave I2C ------*/
const byte I2C_SLAVE_ADDR = 0x20;


/********* Declaracion de funciones internas *********/
void printDate();
void configInitialRTC();
void sendToSlave(DateTime );
uint16_t requestToSlave();

/****************** Funciones Arduino ****************/
/**
 * @brief Configuracion inicial
 * @return nothing
 */
void setup() 
{
  Serial.begin(115200); // Frecuencia en baudios para serial
  Wire.begin();
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
  uint16_t rta = 0;   
  // Obtener fecha actual y mostrar por Serial
  DateTime now = rtc.now();
  printDate(now);
  delay(1000);
  // Enviar data a slave
  sendToSlave(now);
  rta = requestToSlave();
  Serial.print(rta);
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
  Serial.print('/');
  Serial.print(date.month(), DEC);
  Serial.print('/');
  Serial.print(date.day(), DEC);
  Serial.print(" (");
  Serial.print(daysOfTheWeek[date.dayOfTheWeek()]);
  Serial.print(") ");
  Serial.print(date.hour(), DEC);
  Serial.print(':');
  Serial.print(date.minute(), DEC);
  Serial.print(':');
  Serial.print(date.second(), DEC);
  Serial.println();
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
void sendToSlave(DateTime data)
{
  Wire.beginTransmission(I2C_SLAVE_ADDR);
  Wire.write((byte*)&data, sizeof(data));
  Wire.endTransmission();
}

/**
 * @brief Respuesta de Slave I2C
 * @return String con mensaje de Slave
 */
uint16_t requestToSlave()
{
  uint8_t index = 0;  
  uint16_t response = 0;

  Wire.requestFrom(I2C_SLAVE_ADDR, sizeof(response));

  byte* pointer = (byte*)&response;
  while (Wire.available())
  {
    *(pointer + index) = (byte)Wire.read();
    index++;
  }

  return response;
}