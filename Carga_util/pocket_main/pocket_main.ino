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
#include <EEPROM.h>

/*********************** Macros ******************8***/
#define MAX_DATA 33
#define PIN_DAC1 25
#define PIN_DAC2 26

#define MEAS1 1
#define MEAS2 2
#define RTC 3
#define DAC1 4
#define DAC2 5

/****************** Variables globales ***************/ 
/* RTC */
RTC_DS3231 rtc; // Creo objeto RTC_DS1307 rtc;
char datetimeStr[MAX_DATA];  //

/* I2C */
const byte I2C_SLAVE_ADDR = 0x20; // Direccion I2C de Slave
char dataRequest[MAX_DATA]; // Str respuesta de Slave
char dataSend[MAX_DATA]; // Str a enviar de Master

/* UART */
char dataRequestApp[MAX_DATA]; // Str respuesta de Slave
char dataSendApp[MAX_DATA]; // Str a enviar de Master
char dataConcat[MAX_DATA]; // Buf auxiliar para concatenar texto
/* EEPROM */
const int EEPROM_SIZE = 512; // Tamaño de la EEPROM (esto depende de tu modelo de Arduino)
const int THRESHOLD = 480;   // Umbral para enviar datos cuando se llena en un 90%
int currentAddress = 0;      // Dirección actual en la EEPROM
int dataCount = 0;           // Contador de datos guardados
char dataSendEeprom[MAX_DATA]; // Str a enviar EEPROM

/********* Declaracion de funciones internas *********/
void formatDataSend(char* , int, char*);

/* RTC */
void configInitialRTC();
void datetimeNow(char *);

/* I2C */
void sendToSlave(const char*);
void requestFromSlave();

/* UART */
void requestFromAppUart(int*, float*);
void sendToAppUart(const char*);
void commaToSpaceConverter(char *);
//void configFromApp(int , float );

/* DAC */
float value_volt = 0;

/* EEPROM */
void sendToEeprom();

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
  int id = 0;
  float value = 0.0;
  /* Serial */
  // Identificacion por comando en formato CSV
  // * Valor para DAC:ID,value -> 1,1.23 
  // ** ID: 1->Meas1, 2->Meas2, 3->RTC, 4->DAC1, 5->DAC2
  requestFromAppUart(&id, &value);
  //if(id !=0){
  //  configFromApp(id, value);  // Asigno dato segun id    
  //}

  /* RTC */
  datetimeNow(datetimeStr); //Obtengo datetime actual
  
  /* I2C */
  //formatDataSend(dataSend, RTC, datetimeStr);
  sendToSlave("MEAS1"); // Enviar data a slave
  requestFromSlave(); // Respuesta de slave

  /* UART */
  // OBS: Solo enviar datos recibidos de Slave
  commaToSpaceConverter(dataRequest);
  snprintf(dataConcat, MAX_DATA, "%s %s", datetimeStr, dataRequest);  // concateno datos
  formatDataSend(dataSendApp, RTC, dataConcat);
  sendToAppUart(dataSendApp);

  sendToSlave("MEAS2"); // Enviar data a slave
  requestFromSlave(); // Respuesta de slave

  /* UART */
  // OBS: Solo enviar datos recibidos de Slave
  commaToSpaceConverter(dataRequest);
  snprintf(dataConcat, MAX_DATA, "%s %s", datetimeStr, dataRequest);  // concateno datos
  formatDataSend(dataSendApp, RTC, dataConcat);
  sendToAppUart(dataSendApp);

  /* EEPROM */

  delay(100);
}

/**************** Funciones internas  *****************/

void formatDataSend(char* buf, int id, char* str)
{
  snprintf(buf, MAX_DATA, "%d,%s", id, str);
}

/* RTC */
/**
 * @brief Formatear la fecha y hora como "YYYY-MM-DD HH:MM:SS"
 * @return str de fecha y hora
 */
void datetimeNow(char *datetimeStr)
{
  DateTime now = rtc.now(); // Obtener fecha de RTC

  snprintf(datetimeStr, MAX_DATA, "%04d-%02d-%02d %02d:%02d:%02d", 
           now.year(), now.month(), now.day(), 
           now.hour(), now.minute(), now.second());
}

/**
 * @brief Verficación conexion con RTC
 * @return nothing
 */
void configInitialRTC()
{
  /* Verifico deteccion de RTC */
  if (!rtc.begin()){
    //Serial.println(F("NO SE ENCUENTRA RTC"));
    while (1);
  }
  
  /* Fijo datetime en caso de desconexion de la alimentacion */
  if (rtc.lostPower()){
    rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));// Fijar a fecha y hora de compilacion
    //rtc.adjust(DateTime(2025, 9, 8, 22, 23, 0)); // Fijar a fecha y hora específica. En el ejemplo, 3 de Enero de 2024 a las 18:00:00
  }
}

/* I2C */
/**
 * @brief Enviar data a slave I2C
 * @return nothing
 */
void sendToSlave(const char *data)
{
  /* Verificacion de datos a enviar 
  Serial.print("S-Slave: ");
  Serial.println(data); */

  /* Envio datos I2C */
  Wire.beginTransmission(I2C_SLAVE_ADDR);
  // Envía solo los datos válidos
  for (size_t i = 0; i < strlen(data); i++) {
    if (data[i] >= 32 && data[i] <= 126) { // Solo caracteres imprimibles// Cod ASCII
      Wire.write((uint8_t)data[i]);
    } 
    else {
      Wire.write(' '); // Reemplazar caracteres no imprimibles con un espacio
    }
  }
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
    char receivedChar = Wire.read();
    // Filtra los caracteres válidos
    if (receivedChar >= 32 && receivedChar <= 126) { // Solo caracteres imprimibles
      dataRequest[index++] = receivedChar;
    } else {
      // Si encuentras un carácter no imprimible, puedes manejarlo aquí
      dataRequest[index++] = ' '; // Reemplazar caracteres no imprimibles con un espacio
    }
  }
  dataRequest[index] = '\0'; // Terminar el string

  /* Verifico datos recibidos
  Serial.print("R-Slave: ");
  Serial.print(dataRequest);*/
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
/**
 * @brief Respuesta data de app por UART
 * @return id y value
 */
void requestFromAppUart(int* id, float* value)
{
  if (Serial.available()){
    String input_cmd = Serial.readStringUntil('/n');
    // Procesar la cadena recibida en formato "id,value"
    int delimiterIndex = input_cmd.indexOf(','); // Buscar la coma que separa id y value
    if (delimiterIndex > 0) {
      String idStr = input_cmd.substring(0, delimiterIndex); // Extraer el id
      String valueStr = input_cmd.substring(delimiterIndex + 1); // Extraer el value

      // Conversion de formatos y retornos
      *id = idStr.toInt();
      *value = valueStr.toFloat();
    }
  }
}
/*
void configFromApp(int id, float value)
{ 
  int value_map = 0;

  if(id == DAC1){
    value_map = map(value*1000, 0, 3300, 0, 255);
    dacWrite(PIN_DAC1, value_map);  
  }
  else if(id == DAC2){
    value_map = map(value*1000, 0, 3300, 0, 255);
    dacWrite(PIN_DAC2, value_map);  
  }
  else{
    Serial.print("id: ");
    Serial.print(id);
    Serial.println(" ; ID NO RECONOCIDO PARA CONFIG");
  }
}
*/

void commaToSpaceConverter(char *data)
{
  // Recorrer el array para encontrar la coma y reemplazarla por un espacio
  for (int i = 0; i < strlen(data); i++) {
      if (data[i] == ',') {
          data[i] = ' ';
          break; // Salir del bucle después de encontrar y reemplazar la coma
      }
  }
}

/* EEPROM */
void sendToEeprom()
{
  // Almacenar en EEPROM
  if (currentAddress < EEPROM_SIZE) {
    EEPROM.put(currentAddress, dataSendEeprom);
    currentAddress += sizeof(dataSendEeprom);
    dataCount++;
  }
}
