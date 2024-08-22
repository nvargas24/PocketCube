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

/****************** Variables globales ***************/ 
/*----- Comunicacion master-slave I2C ------*/
char receivedData[20]; // OBS: Ver tamanio de buffer
char responseData[20];

volatile bool dataReceived = false;
volatile byte index = 0;


float meas_temp = 0.0;
float meas_current = 0.0;

/********* Declaracion de funciones internas *********/
void receiveEvent(int bytes);
void requestEvent();

float readTemp();
float readCurrent();

/****************** Funciones Arduino ****************/
/**
 * @brief Configuracion inicial
 * @return nothing
 */
void setup()
{
  /* Serial */
  Serial.begin(115200);
  
  /* SPI */
  pinMode(MISO, OUTPUT);
  //SPI.begin();
  SPCR |= _BV(SPE); // Habilita SPI en modo esclavo
  SPI.attachInterrupt();
}

/**
 * @brief Interrupcion al recibir data de Master por SPI
 * @return nothing
 */
ISR(SPI_STC_vect) 
{
  receivedData[index++] = SPDR; // Lee el byte recibido

  if (index >= sizeof(receivedData) || receivedData[index-1] == '\0') {
    dataReceived = true;
    index = 0; // Resetea el índice
  }

  /* Enviar la medición de temperatura después de recibir el dato
  if (dataReceived) {
    while(responseData[index] != '\0') {
      SPDR = responseData[index++];
      delay(10); // Pequeña pausa para asegurar la sincronización
    }
    index = 0; // Resetea el índice para la próxima transmisión
  }
  */
}


/**
 * @brief Bucle de ejecucion de programa principal
 * @attention solo RTC por el momento
 * @return nothing
 */
void loop() 
{
  float temperature = readTemp();
  char tempStr[10];
    
  if (dataReceived) {
    // Data recibidad de Master
    Serial.print("Mensaje recibido: ");
    Serial.println(receivedData);

    // Data respuesta a Master
    //dtostrf(temperature, 6, 2, tempStr); // Convierte el valor de temperatura a cadena con 2 decimales
    //snprintf(responseData, sizeof(responseData), "%s, %s", date, tempStr);

    dataReceived = false;
  }

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
