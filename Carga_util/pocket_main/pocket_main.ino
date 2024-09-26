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

/*********************** Macros *********************/
#define I2C_SLAVE_ADDR 0x20
#define MAX_DATA_I2C 33
#define MAX_DATA_UART 40
#define MAX_DATA_RTC 20
#define PIN_DAC1 25
#define PIN_DAC2 26
#define MAX_EEPROM 1024
#define THRESHOLD (MAX_EEPROM*0.99) //Umbral para enviar datos cuando se llena en un 90%
#define MAX_SIZE_MEAS 7

#define TOTAL_EEPROM 0
#define USED_EEPROM 1
#define FREE_EEPROM 2

#define MEAS1 1
#define MEAS2 2
#define RTC 3
#define EEPROM_FREE 4
#define EEPROM_DATA 5
#define STATE 6

/****************** Variables globales ***************/ 
/* RTC */
RTC_DS3231 rtc; // Creo objeto RTC_DS1307 rtc;
char datetimeStr[MAX_DATA_RTC];  //

/* I2C */
char dataRequest[MAX_DATA_I2C]; // Str respuesta de Slave
char dataSend[MAX_DATA_I2C]; // Str a enviar de Master

/* UART */

/* EEPROM */
int address = 0;      // Dirección actual en la EEPROM

/********* Declaracion de funciones internas *********/
void formatDataSend(char* , int, char*);
void formatDataSendLong(int, char*);

/* RTC */
void configInitialRTC();
void datetimeNow(char *);

/* I2C */
void sendToSlave(const char*);
int requestFromSlave();

/* UART */
void requestFromAppUart(int*, float*);
void sendToAppUart(const char*);
void commaToSpaceConverter(char *);
//void configFromApp(int , float );

/* EEPROM */
void writeEEPROM(char*, size_t);
int stageUsedEEPROM();
void clearEEPROM();
void readEEPROM(char*);
int analyzeEEPROMStorage(int);

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
  char dataConcat[MAX_DATA_UART]; // Buf auxiliar para concatenar texto
  char meas1[MAX_SIZE_MEAS];
  char meas2[MAX_SIZE_MEAS];
  int sizeEEPROM = 0;
  char strAux[MAX_DATA_UART];
  char dataSendApp[MAX_DATA_UART]; // Str a enviar de Master a APP
  size_t sizeDataConcat = 0;
  char dataReadEEPROM[MAX_EEPROM];
  char aux_eeprom[MAX_EEPROM];

  /* Serial */
  // Identificacion por comando en formato CSV
  // * Valor para DAC:ID,value -> 1,1.23 
  // ** ID: 1->Meas1, 2->Meas2, 3->RTC, 4->DAC1, 5->DAC2
  requestFromAppUart(&id, &value);
  //if(id !=0){
  //  configFromApp(id, value);  // Asigno dato segun id    
  //}

  formatDataSend(dataSendApp, STATE, "Read MEASURES");
  sendToAppUart(dataSendApp);   
  
  /* RTC */
  datetimeNow(datetimeStr); //Obtengo datetime actual
  
  /* I2C MEAS1 */
  sendToSlave("MEAS1"); // Enviar data a slave
  requestFromSlave(); // Respuesta de slave
  strcpy(meas1, dataRequest);
  commaToSpaceConverter(meas1);

  /* I2C MEAS2 */
  sendToSlave("MEAS2"); // Enviar data a slave
  requestFromSlave(); // Respuesta de slave
  strcpy(meas2, dataRequest);
  commaToSpaceConverter(meas2);

  /* ENVIO MEDICIONES A APP */
  snprintf(dataConcat, MAX_DATA_UART, "%s %s %s", datetimeStr, meas1, meas2);  // concateno datos
  sizeDataConcat = strlen(dataConcat);
  formatDataSend(dataSendApp, RTC, dataConcat);
  sendToAppUart(dataSendApp);

  /* EEPROM */
  sizeEEPROM = analyzeEEPROMStorage(FREE_EEPROM);
  snprintf(strAux, MAX_DATA_UART, "%d", sizeEEPROM); // Conversion de int a str
  formatDataSend(dataSendApp, EEPROM_FREE, strAux);
  sendToAppUart(dataSendApp);


  if(sizeEEPROM >= sizeDataConcat){
    formatDataSend(dataSendApp, STATE, "Write EEPROM");
    sendToAppUart(dataSendApp);    
    writeEEPROM(dataConcat, sizeDataConcat);  // solo guardo datetime, id y value de mediciones
  }
  else{
    formatDataSend(dataSendApp, STATE, "Read EEPROM"); // Notificacion de vacio de EEPROM
    sendToAppUart(dataSendApp);     
    readEEPROM(dataReadEEPROM);

    //snprintf(aux_eeprom, MAX_EEPROM, "%d,%s", EEPROM_DATA, dataReadEEPROM);
    formatDataSendLong(EEPROM_DATA, dataReadEEPROM);
    sendToAppUart(dataReadEEPROM);

    formatDataSend(dataSendApp, STATE, "Clear EEPROM"); // Notificacion de vacio de EEPROM
    sendToAppUart(dataSendApp); 
    clearEEPROM();
    memset(dataReadEEPROM, 0, MAX_EEPROM);  // Rellena el array con ceros
    address = 0; // ubico en primera celda de EEPROM, evitando data cortada
    formatDataSend(dataSendApp, STATE, "EEPROM OK"); // Notificacion de vacio de EEPROM
    sendToAppUart(dataSendApp); 
  }

  delay(100);
}

/**************** Funciones internas  *****************/
void formatDataSendLong(int id, char* str)
{
  char text[3];
  int textoLen;
  int arrayLen;

  snprintf(text, 3, "%d,", id);

  textoLen = strlen(text);
  arrayLen = strlen(str);
  
  for (int i = arrayLen; i >= 0; i--) {
    str[i + textoLen] = str[i]; // Desplaza el contenido
  }

  // Copia el nuevo texto al inicio del array
  for (int i = 0; i < textoLen; i++) {
    str[i] = text[i];
  }

}
void formatDataSend(char* buf, int id, char* str)
{
  snprintf(buf, MAX_DATA_UART, "%d,%s", id, str);
}

/* RTC */
/**
 * @brief Formatear la fecha y hora como "YYYY-MM-DD HH:MM:SS"
 * @return str de fecha y hora
 */
void datetimeNow(char *datetimeStr)
{
  DateTime now = rtc.now(); // Obtener fecha de RTC

  snprintf(datetimeStr, MAX_DATA_RTC, "%04d-%02d-%02d %02d:%02d:%02d", 
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
    rtc.adjust(DateTime(2024, 9, 15, 21, 12, 0)); // Fijar a fecha y hora específica. En el ejemplo, 3 de Enero de 2024 a las 18:00:00
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
int requestFromSlave()
{
  uint8_t index = 0;  
  char receivedChar;
  int size_rta = 0;

  /* Preparo Master para recibir respuesta de Slave  */
  Wire.requestFrom(I2C_SLAVE_ADDR, sizeof(dataRequest)); // Solicitud a slave

  while (Wire.available() && (index < MAX_DATA_I2C)) {
    receivedChar = Wire.read();
    // Filtra los caracteres válidos
    if (receivedChar >= 32 && receivedChar <= 126) { // Solo caracteres imprimibles
      dataRequest[index] = receivedChar;
      index++;
    } 
    else {
      // Si encuentras un carácter no imprimible
      break;
    }
  }
  dataRequest[index] = '\0'; // Terminar el string

  size_rta = strlen(dataRequest);

  /* Verifico datos recibidos
  Serial.print("R-Slave: ");
  Serial.print(dataRequest);*/
  return size_rta;
}

/* UART */
/**
 * @brief Enviar data app por UART, limita solo caracteres
 */
void sendToAppUart(const char* data)
{
    //Enviar solo la parte válida del mensaje
    for (int i = 0; i < strlen(data); i++) {
      if (data[i] >= 32 && data[i] <= 126) { // Solo caracteres imprimibles// Cod ASCII
        Serial.print(data[i]);
      }
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

/**
 * @brief Conversion de comas a espacios para adjuntar a trama de datos
 * @return None
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
/**
 * @brief Cargar datos en memoria EEPROM
 * @return None
 */
void writeEEPROM(char* data, size_t length)
{
  char dataWrite[length+2]; // considero 2 fines, ";": fin de msj "/0" fin de array

  snprintf(dataWrite, length+2, "%s;", data);
  
  // Escribe los datos en la EEPROM
  for (int i = 0; i < strlen(dataWrite); i++) {
    EEPROM.write(address++, dataWrite[i]);
  }
  // Escribe el delimitador ';' al final
  if (address < MAX_EEPROM) {
    EEPROM.write(address, ';');
  }
}

void readEEPROM(char* data)
{ 
  int address = 0;
  int index = 0;

  // Lee los datos desde la EEPROM hasta llenar el array o llegar al final de la EEPROM
  while (address < MAX_EEPROM && index < MAX_EEPROM - 1) {
    char c = EEPROM.read(address++);
    data[index++] = c;
  }

  // Añade un carácter nulo al final del array para que sea una cadena de texto válida
  data[index] = '\0';
}

/**
 * @brief Vaciar memoria EEPROM
 * @return None
 */
void clearEEPROM() 
{
  //Serial.println("Vaciando EEPROM...");
  for (int i = 0; i < MAX_EEPROM; i++) {
    EEPROM.write(i, 0xFF);  // Escribir valor por defecto (0xFF) en toda la EEPROM
  }
  //Serial.println("EEPROM vaciada.");
}

/**
 * @brief Calculo de espacio de memoria EEPROM interna utilizada
 * @return used: espacio de memoria utilizado
 */
int stageUsedEEPROM()
{
  int used = 0;
  for (int i = 0; i < EEPROM.length(); i++) {
    if (EEPROM.read(i) != 0xFF) {  // La EEPROM vacía tiene el valor 0xFF
      used++;
    }
  }
  return used; 
}

int analyzeEEPROMStorage(int type)
{
  int totalEEPROM = EEPROM.length();
  int usedEEPROM = stageUsedEEPROM();
  int freeEEPROM = totalEEPROM - usedEEPROM;


  if(type == TOTAL_EEPROM){
    return totalEEPROM;
  }
  else if(type == USED_EEPROM){
    return usedEEPROM;
  }
  else if(type == FREE_EEPROM){
    return freeEEPROM;
  }

}
