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

/*********************** Macros ******************8***/
#define MAX_DATA_I2C 33

/****************** Variables globales ***************/ 
/* I2C */
const byte I2C_SLAVE_ADDR = 0x20;
char dataRequest[MAX_DATA_I2C];
char dataReceive[MAX_DATA_I2C];

/* RTC */
char datetime[20];

/* Meas */
float meas_temp = 0.0;
float meas_current = 0.0;

/********* Declaracion de funciones internas *********/
/* I2C */
void receiveEvent(int bytes);
void requestEvent();

/* Meas */
float readTemp();
float readCurrent();

/****************** Funciones Arduino ****************/
/**
 * @brief Configuracion inicial
 * @return nothing
 */
void setup()
{
  Serial.begin(115200); // Frecuencia en baudios para serial

  /* Eventos I2C */
  Wire.begin(I2C_SLAVE_ADDR);
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);
}

/**
 * @brief Bucle de ejecucion de programa principal
 * @attention solo RTC por el momento
 * @return nothing
 */
void loop() 
{
  /* Serial */
  // Identificacion por comando en formato CSV
  // * Valor para DAC:ID,value -> 1,1.23 
  // ** ID: 1->Meas1, 2->Meas2, 3->RTC

  /* Meas */
  meas_temp = readTemp(); 
  meas_current = readCurrent();
  delay(1000);
}

/**
 * @brief Evento de recepcion de data
 * @return nothing
 */
void receiveEvent(int bytes)
{
  int index = 0;

  /* Preparo Slave para recibir data  */
  while (Wire.available() && index < sizeof(dataReceive) - 1) {
    dataReceive[index++] = Wire.read();
  }
  dataReceive[index] = '\0'; // Terminar el string

  /* Verifico datos recibidos */
  Serial.print("R-Master: ");
  Serial.println(dataReceive);

  /* Guardo data recibida en otra variable especifica */
  strcpy(datetime, dataReceive);
}

/**
 * @brief Evento de respuesta de data a master
 * @return nothing
 */
void requestEvent()
{
  char tempStr[10];
  char currentStr[10];

  /*Conversion de float a str*/
  // Necesario ya que arduino no reconoce float para usar en snprintf
  dtostrf(meas_temp, 5, 2, tempStr);
  dtostrf(meas_current, 5, 2, currentStr); 

  snprintf(dataRequest, sizeof(dataRequest), "I:%smA,Dt:%s", currentStr, datetime);

  /* Verificacion de datos a enviar */
  Serial.print("S-Master: ");
  Serial.println(dataRequest);

  /* Envio respuesta por I2C */
  Wire.write(dataRequest);
}

/* Funciones ejemplos de lectura */
// conectar algun sensor para testear realtime
float readTemp()
{
  return 24.7;
}

float readCurrent()
{
  return 21.34;
}