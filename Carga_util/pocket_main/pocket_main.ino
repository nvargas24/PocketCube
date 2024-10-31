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
#define I2C_SLAVE_ADDR 0x08
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
#define EEPROM_USED 4
#define EEPROM_DATA 5
#define STATE 6
#define TIMER 7

#define STR_MEAS1 '1'
#define STR_MEAS2 '2'

#define STOP_TIMER 0
#define INIT_TIMER 1


/****************** Variables globales ***************/ 
/* RTC */
RTC_DS3231 rtc; // Creo objeto RTC_DS1307 rtc;
char datetimeStr[MAX_DATA_RTC];  //

/* I2C */
char dataRequest[MAX_DATA_I2C]; // Str respuesta de Slave
char dataSend[MAX_DATA_I2C]; // Str a enviar de Master

/* UART */
int serial_id = 0;
int value = 0;
char lastRTC[MAX_DATA_I2C] = ""; // Buffer para almacenar el último mensaje enviado
char lastState[MAX_DATA_I2C] = ""; // Buffer para almacenar el último mensaje enviado

/* TIMER */
bool i2cActive = false;
bool timerActive = true;

/* EEPROM */
int address = 0;      // Dirección actual en la EEPROM

/********* Declaracion de funciones internas *********/
void formatDataSend(char* , int, char*);
void formatDataSendLong(int, char*);
void filterValue(char *);

/* RTC */
void configInitialRTC();
void datetimeNow(char *);

/* I2C */
void sendToSlave(const char*);
void sendToSlaveC(char);
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
  Serial.begin(9600); // Frecuencia en baudios para serial
  Wire.begin(); // Inicializo comunicacion I2C
  //Wire.setClock(100000); // Configurar la frecuencia I2C a 100 kHz
  //configInitialRTC(); // Inicializo configuiracion de RTC
  configTimer();
  delay(1000); 
}

/**
 * @brief Bucle de ejecucion de programa principal
 * @attention solo RTC por el momento
 * @return nothing
 */
void loop() 
{
  char dataConcat[MAX_DATA_UART]; // Buf auxiliar para concatenar texto
  char meas1[MAX_SIZE_MEAS];
  char meas2[MAX_SIZE_MEAS];
  //int sizeEEPROM_total = 0;
  //int sizeEEPROM_used = 0;
  //int sizeEEPROM_used_per = 0;
  //int sizeEEPROM_free = 0;
  //char strAux[MAX_DATA_UART];
  size_t sizeDataConcat = 0;
  //char dataReadEEPROM[MAX_EEPROM];
  //char aux_eeprom[MAX_EEPROM];

  i2cActive = false;
  /* Serial */
  requestFromAppUart(&serial_id, &value);
  delay(100);
  //Serial.print(serial_id);
  //Serial.print(",");
  //Serial.println(value);
  if(serial_id !=0){
    configFromApp(serial_id, value);  // Asigno dato segun id    
  }

  sendToAppUart(STATE, "Read MEASURES");   
  
  /* RTC */
  //datetimeNow(datetimeStr); //Obtengo datetime actual
  /* ENVIO DATETIME */
  //formatDataSend(RTCSendApp, RTC, );
  sendToAppUart(RTC, "2024-10-27 15:30:45");
    
  if(i2cActive){
    /* I2C MEAS1 */
    /* Envio datos I2C */
    sendToSlaveC(STR_MEAS1); // Solicitud de data en pin PB3
    delay(100); // Pequeña espera para asegurar que el esclavo reciba el dato
    requestFromSlave(); // Respuesta de slave
    //strcpy(meas1, dataRequest);
    //commaToSpaceConverter(meas1);
    //filterValue(meas1);

    /* I2C MEAS2 */
    sendToSlaveC(STR_MEAS2); // Enviar data a slave
    delay(100); // Pequeña espera para asegurar que el esclavo reciba el dato
    requestFromSlave(); // Respuesta de slave
    //strcpy(meas2, dataRequest);
    //commaToSpaceConverter(meas2);
    //filterValue(meas2);
  }

  /* ENVIO MEDICIONES A APP 
    snprintf(dataConcat, MAX_DATA_UART, "%s %s %s", datetimeStr, meas1, meas2);  // concateno datos
    sizeDataConcat = strlen(dataConcat);
    formatDataSend(dataSendApp, RTC, dataConcat);
    sendToAppUart(dataSendApp);*/


  /* EEPROM
    sizeEEPROM_total = analyzeEEPROMStorage(TOTAL_EEPROM);
    sizeEEPROM_used = analyzeEEPROMStorage(USED_EEPROM);
    sizeEEPROM_free = analyzeEEPROMStorage(FREE_EEPROM);
    sizeEEPROM_used_per = (sizeEEPROM_used*100.0)/sizeEEPROM_total;

    snprintf(strAux, MAX_DATA_UART, "%d", sizeEEPROM_used_per); // Conversion de int a str
    formatDataSend(dataSendApp, EEPROM_USED, strAux);
    sendToAppUart(dataSendApp);

    if(sizeEEPROM_free >= sizeDataConcat){
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
      //clearEEPROM();
      memset(dataReadEEPROM, 0, MAX_EEPROM);  // Rellena el array con ceros
      address = 0; // ubico en primera celda de EEPROM, evitando data cortada
      formatDataSend(dataSendApp, STATE, "EEPROM OK"); // Notificacion de vacio de EEPROM
      sendToAppUart(dataSendApp); 
    }
  */
}

/**************** Funciones internas  *****************/
void filterValue(char *str)
{
  // Encuentra la posición de la coma
  char *commaPtr = strchr(str, ','); // Busca la coma en el array

  // Si se encuentra la coma, desplaza el resto del array hacia la izquierda
  if (commaPtr != nullptr) {
      // Desplaza el contenido del array a la izquierda
      int offset = commaPtr - str; // Calcula el desplazamiento
      strcpy(str, commaPtr+1); // Copia el resto del array sobre el inicio
  }
}

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
  Serial.println(F("Configuracion RTC INIT"));
  /* Verifico deteccion de RTC */
  while(!rtc.begin()){
    Serial.println(F("NO SE ENCUENTRA RTC"));
    //while (1);
  }
  Serial.println(F("ConfRTC 2"));
  /* Fijo datetime en caso de desconexion de la alimentacion */
  if (rtc.lostPower()){
    rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));// Fijar a fecha y hora de compilacion
    rtc.adjust(DateTime(2024, 9, 15, 21, 12, 0)); // Fijar a fecha y hora específica. En el ejemplo, 3 de Enero de 2024 a las 18:00:00
  }
  Serial.println(F("Configuracion RTC FIN"));
}

/* I2C */
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
 * @brief Enviar caracter a slave I2C
 * @return nothing
 */
void sendToSlaveC(char c){
  Wire.beginTransmission(I2C_SLAVE_ADDR); // Comienza la transmisión hacia el esclavo con dirección 8
  Wire.write(c); // Envía el carácter "1" - lectura PB3
  Wire.endTransmission(); // Finaliza la transmisión
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

  /* Verifico datos recibidos*/
  //Serial.print("R-Slave: ");
  Serial.println(dataRequest);
  return size_rta;
}

/* UART */
/**
 * @brief Enviar data app por UART, limita solo caracteres
 */
void sendToAppUart(int serial_id, const char* data)
{
    bool flag_rtc = false;
    bool flag_state = false;
    char dataSendApp[MAX_DATA_UART]; // Str a enviar de Master a APP

    formatDataSend(dataSendApp, serial_id, data);
    
    if((serial_id == RTC) && (strcmp(data, lastRTC)!=0)){
      flag_rtc = true;
    }
    else if((serial_id == STATE) && (strcmp(data, lastState)!=0)){
      flag_state = true;
    }

    if(flag_rtc==false && flag_state==false){
      //Enviar solo la parte válida del mensaje
      for (int i = 0; i < strlen(data); i++) {
        if (data[i] >= 32 && data[i] <= 126) { // Solo caracteres imprimibles// Cod ASCII
          Serial.print(data[i]);
        }
      }
      Serial.println();  // Envía un salto de línea al final      
    }
    // Copia el nuevo mensaje en el buffer `ultimoMensaje`
    //strncpy(lastMsj, data, MAX_DATA_I2C - 1);
    //lastMsj[MAX_DATA_I2C - 1] = '\0';  // Asegura el carácter nulo al final  
}
/**
 * @brief Respuesta data de app por UART
 * @return id y value
 */
void requestFromAppUart(int* id, int* value)
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
      *value = valueStr.toInt();
    }
  }
}
/**
 * @brief Configuracion a realizar en Arduino
 */
void configFromApp(int serial_id, int cmd)
{ 
  if(serial_id==TIMER){
    if(cmd==INIT_TIMER){
      timerActive = true;
    }
    else if(cmd==STOP_TIMER){
      timerActive = false;
    }
  }
  else{
    Serial.print("id: ");
    Serial.print(serial_id);
    Serial.println(" ; ID NO RECONOCIDO PARA CONFIG");
  }
}

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
  //if (address < MAX_EEPROM) {
  //  EEPROM.write(address, ';');
  //}
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
    EEPROM.update(i, 0xFF);  // Escribir valor por defecto (0xFF) en toda la EEPROM
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

/**
 * @brief Configuración del temporizador 1
 */
void configTimer()
{
  noInterrupts();           // Desactivar interrupciones
  TCCR1A = 0;               // Limpiar registros
  TCCR1B = 0;
  TCNT1 = 0;                // Inicializar el contador del temporizador
  OCR1A = 15624;            // Valor de comparación para 1 segundo a 16 MHz con prescaler de 1024
  TCCR1B |= (1 << WGM12);   // Modo CTC
  TCCR1B |= (1 << CS12) | (1 << CS10); // Prescaler de 1024
  TIMSK1 |= (1 << OCIE1A);  // Habilitar interrupción por comparación
  interrupts();             // Activar interrupciones
}

/**
 * @brief Interrupción del temporizador 1
 */
ISR(TIMER1_COMPA_vect) 
{
  if(timerActive){
    i2cActive = true;
  }
  else{
    i2cActive = false;
  }
}
