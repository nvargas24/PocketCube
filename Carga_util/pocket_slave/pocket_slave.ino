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
#include <avr/io.h>
#include <avr/interrupt.h>

/*********************** Macros ******************8***/
#define MAX_DATA 33

#define MEAS1 1
#define MEAS2 2
#define RTC 3
#define TIMER 6

/****************** Variables globales ***************/ 
/* I2C */
const byte I2C_SLAVE_ADDR = 0x20;
char dataRequest[MAX_DATA];
char dataReceive[MAX_DATA];

/* UART */
char dataRequestApp[MAX_DATA]; // Str respuesta de Slave
char dataSendApp[MAX_DATA]; // Str a enviar de Master

/* RTC */
char datetime[20];

/* Meas */
float meas1_data = 0.0;
float meas2_data = 0.0;
char dataStr[10];

/* TIMER */
volatile unsigned long seconds = 0;  // Variable para contar los segundos

/********* Declaracion de funciones internas *********/
/* I2C */
void receiveEvent(int bytes);
void requestEvent();

/* UART */
void sendToAppUart(const char*);

/* Meas */
float readAdc1();

void formatSendCmd(char*, int, const char*);

/* TIMER */
void configTimer();
/****************** Funciones Arduino ****************/
/**
 * @brief Configuracion inicial
 * @return nothing
 */
void setup()
{
  Serial.begin(115200); // Frecuencia en baudios para serial
  configTimer();
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
  meas1_data = readAdc1(A1);   
  
  /* TIMER */
  if (seconds >= 1000){
    formatSendCmd(dataSendApp, TIMER, "----- TIMER ---");
    sendToAppUart(dataSendApp);
    seconds = 0;
  }
  delay(100);
}

/* I2C */
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

  /* Verifico datos recibidos
  Serial.print("R-Master: ");
  Serial.println(dataReceive);*/

  /* Guardo data recibida en otra variable especifica */
  //strcpy(datetime, dataReceive);
}

/**
 * @brief Evento de respuesta de data a master
 * @return nothing
 */
void requestEvent()
{
  dtostrf(meas1_data, 5, 2, dataStr);// Necesario ya que arduino no reconoce float para usar en snprintf
  formatSendCmd(dataRequest, MEAS1, dataStr); 
  
  /* Serial */
  formatSendCmd(dataSendApp, MEAS1, dataStr);
  sendToAppUart(dataSendApp);  
  /* Verificacion de datos a enviar
  Serial.print("S-Master: ");
  Serial.println(dataRequest);*/

  /* Envio respuesta por I2C */
  // Envía solo los datos válidos
  for (size_t i = 0; i < strlen(dataRequest); i++) {
    if (dataRequest[i] >= 32 && dataRequest[i] <= 126) { // Solo caracteres imprimibles// Cod ASCII
      Wire.write((uint8_t)dataRequest[i]);
    } 
    else {
      Wire.write(' '); // Reemplazar caracteres no imprimibles con un espacio
    }
  }


}

/* UART */
/**
 * @brief Enviar data app por UART
 */
void sendToAppUart(const char* data)
{
    //Enviar solo la parte válida del mensaje
    for (int i = 0; i < strlen(data); i++) {
      Serial.print(data[i]);
    }
    Serial.println();  // Envía un salto de línea al final
}

/* Meas*/
// conectar algun sensor para testear realtime
float readAdc1(int adcPin)
{
  int adc1Value = analogRead(adcPin);  // Leer el valor de ADC1 (A1)
  float voltaje = adc1Value*(5.0/1023);

  return voltaje;
}

void formatSendCmd(char* buf, int id, const char* data)
{
  snprintf(buf, MAX_DATA, "%d,%s", id, data);
}

/* TIMER */
void configTimer()
{
// Configura Timer0 para generar una interrupción cada segundo
  cli();  // Deshabilita las interrupciones globales

  // Configura Timer0 para CTC (Clear Timer on Compare Match) mode
  TCCR0A = (1 << WGM01);  // Modo CTC (Clear Timer on Compare Match)
  TCCR0B = (1 << CS02) | (1 << CS00);  // Prescaler 1024

  // Configura el valor de comparación para 1 segundo
  // (16 MHz / 1024) - 1 = 156 (aprox 1 segundo)
  OCR0A = 156;  

  // Habilita la interrupción de comparación de Timer0
  TIMSK0 = (1 << OCIE0A);  

  sei();  // Habilita las interrupciones globales

}

// Interrupción de Timer0
ISR(TIMER0_COMPA_vect) {
  seconds++;  // Incrementa el contador de segundos
}
