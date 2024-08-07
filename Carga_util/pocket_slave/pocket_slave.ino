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

/****************** Variables globales ***************/ 
/*----- Comunicacion master-slave I2C ------*/
const byte I2C_SLAVE_ADDR = 0x20;
uint16_t data = 0;
char response[40]; // DateTime+medicion
char receivedStr[20]; // OBS: Ver tamanio de buffer

char datetime[20];
float meas_temp = 0.0;
float meas_current = 0.0;

/********* Declaracion de funciones internas *********/
void receiveEvent(int bytes);
void requestEvent();

float read_temp();
float read_current();

/****************** Funciones Arduino ****************/
/**
 * @brief Configuracion inicial
 * @return nothing
 */
void setup()
{
  Serial.begin(115200);

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
  /*lectura de corriente y uso de LTC3105*/
  // Ejemplos de mediciones 
  meas_temp = readTemp(); 
  meas_current = readCurrent();
  delay(1000);

  // OBS.: Considerar usar un .JSON si son muchos datos
}

/**
 * @brief Evento de recepcion de data
 * @return nothing
 */
void receiveEvent(int bytes)
{
  int index = 0;

  while (Wire.available() && index < sizeof(receivedStr) - 1) {
    receivedStr[index++] = Wire.read();
  }
  receivedStr[index] = '\0'; // Terminar el string

  // Procesar el string recibido
  Serial.print("RData from Master: ");
  Serial.println(receivedStr);

  strcpy(datetime, receivedStr);
}

/**
 * @brief Evento de respuesta de data a master
 * @return nothing
 */
void requestEvent()
{
  snprintf(response, sizeof(response), "Temp.: %.2f, Current:%.2f, DateTime:%s", meas_temp, meas_current, datetime);
  Wire.write((const uint8_t*)response, strlen(response));

  Serial.print("SData to Master: ");
  Serial.println(response);
}

/* Funciones ejemplos de lectura */
// conectar algun sensor para testear realtime
float read_temp()
{
  return 24.7;
}

float read_current()
{
  return 210.34;
}
