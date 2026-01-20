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
 */

/****** Encabezados *****/
#include <Wire.h>

/*********************** Macros *********************/
#define I2C_SLAVE_ADDR 0x08
#define MAX_DATA_I2C 33

#define HOW_CP 8

#define STR_MEAS1 '1'
#define STR_COUNT '8'

/****************** Variables globales ***************/ 
/* I2C */
char dataRequest[MAX_DATA_I2C]; // Str respuesta de Slave

/* UART */
int serial_id = 0;
int value = 0;

/* TIMER */
bool i2cActive = false;

/********* Declaracion de funciones internas *********/
void filterValue(char *);

/* I2C */
void sendToSlaveC(char);
int requestFromSlave();

/* UART */
void requestFromAppUart(int*, int*);
void sendToAppUart(const char*);

/****************** Funciones Arduino ****************/
/**
 * @brief Configuracion inicial
 * @return nothing
 */
void setup() 
{
  Serial.begin(9600); // Frecuencia en baudios para serial
  Wire.begin(); // Inicializo comunicacion I2C
  delay(1000); 
}

/**
 * @brief Bucle de ejecucion de programa principal
 * @attention solo RTC por el momento
 * @return nothing
 */
void loop() 
{
  i2cActive = false;
  /* Serial */
  requestFromAppUart(&serial_id, &value);
  delay(100);

  if(serial_id !=0){
    configFromSerial(serial_id, value);  // Asigno dato segun id    
  }

  if(i2cActive){
    Serial.println("Arduino solicita a ATtiny CPS");
    /* I2C MEAS1 */
    /* Envio datos I2C */
    sendToSlaveC(STR_MEAS1); // Solicitud I2C pin PB3
    delay(100);
    requestFromSlave(); // Captura rta de Slave I2C
    filterValue(dataRequest); // Extrae el valor después de la coma
    
    Serial.print("ATtiny conto: ");
    Serial.print(dataRequest);
    Serial.println(" pulsos");

    serial_id = 0;
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

/**
 * @brief Enviar caracter a slave I2C
 * @return nothing
 */
void sendToSlaveC(char c){
  Wire.beginTransmission(I2C_SLAVE_ADDR); // Comienza la transmisión hacia el esclavo con dirección 8
  Wire.write(c); // Envía el carácter "1" - lectura PB3
  Wire.endTransmission(); // Finaliza la transmisión
  //Serial.print("-------Solicitud: ");
  //Serial.println(c);
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
void configFromSerial(int serial_id, int cmd)
{ 
  if(serial_id == HOW_CP){
    i2cActive = true;
  }

  else{
    Serial.print("id: ");
    Serial.print(serial_id);
    Serial.println(" ; ID NO RECONOCIDO PARA CONFIG");
  }
}
