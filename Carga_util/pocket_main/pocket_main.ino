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

/*********************** Macros *********************/
#define I2C_SLAVE_ADDR 0x08
#define MAX_DATA_I2C 33
#define MAX_DATA_UART 40
#define MAX_SIZE_MEAS 7

#define MEAS1 1
#define STATE 6
#define TIMER 7

#define STR_MEAS1 '1'

#define STOP_TIMER 0
#define INIT_TIMER 1


/****************** Variables globales ***************/ 
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

/********* Declaracion de funciones internas *********/
void formatDataSend(char* , int, char*);
void formatDataSendLong(int, char*);
void filterValue(char *);

/* I2C */
void sendToSlave(const char*);
void sendToSlaveC(char);
int requestFromSlave();

/* UART */
void requestFromAppUart(int*, float*);
void sendToAppUart(const char*);
void commaToSpaceConverter(char *);


/****************** Funciones Arduino ****************/
/**
 * @brief Configuracion inicial
 * @return nothing
 */
void setup() 
{
  Serial.begin(9600); // Frecuencia en baudios para serial
  Wire.begin(); // Inicializo comunicacion I2C
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
  size_t sizeDataConcat = 0;
  char dataSendApp[MAX_DATA_UART];
  char dateTimeRTC[MAX_DATA_UART];

  i2cActive = false;
  /* Serial */
  requestFromAppUart(&serial_id, &value);
  delay(100);

  if(serial_id !=0){
    configFromApp(serial_id, value);  // Asigno dato segun id    
  }
  formatDataSend(dataSendApp, STATE, "Read MEASURES");
  sendToAppUart(dataSendApp);   
  
    
  if(i2cActive){
    /* I2C MEAS1 */
    /* Envio datos I2C */
    Serial.println("Test..........");
    sendToSlaveC(STR_MEAS1); // Solicitud de data en pin PB3
    delay(100); // Pequeña espera para asegurar que el esclavo reciba el dato
    requestFromSlave(); // Respuesta de slave
    filterValue(dataRequest);
    snprintf(meas1, MAX_DATA_UART, "%s %s", datetimeStr, dataRequest);
    formatDataSend(dataSendApp, MEAS1, meas1);
    sendToAppUart(dataSendApp);

  }
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
  Serial.println("1");
  Wire.beginTransmission(I2C_SLAVE_ADDR); // Comienza la transmisión hacia el esclavo con dirección 8
  Serial.println("2");
  Wire.write(c); // Envía el carácter "1" - lectura PB3
  Serial.println("3");
  Wire.endTransmission(); // Finaliza la transmisión
  Serial.print("Envio: ");
  Serial.println(c);
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
  //Serial.println(dataRequest);
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
    //Serial.println("Timer active");
  }
  else{
    i2cActive = false;
  }
}
