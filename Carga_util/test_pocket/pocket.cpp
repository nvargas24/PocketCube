#include "pocket.h"

/****************** Variables globales ***************/ 
/* I2C */
char dataRequest[MAX_DATA_I2C]; // Str respuesta de Slave

/* UART */
int serial_id = NO_CMD;
int value = 0;

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
  // Enviar ID de APP
  Serial.print(SEND_APP);
  Serial.print(",");

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
    String input_cmd = Serial.readStringUntil('\n');
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
void requestI2C(const uint8_t cmd)
{ 
  /* I2C Contador de pulsos por segundos */
  if(cmd == CPM){
    Serial.println("CP acumulado en ultimo minuto"); 
    sendToSlaveC(R_CPM); // Solicitud I2C pin PB3
    delay(10);

    requestFromSlave(); // Captura rta de Slave I2C
    filterValue(dataRequest); // Extrae el valor después de la coma
    Serial.print("----> CPM: ");
  }
  /* I2C CPS acumulados */
  else if(cmd == CPS_NOW){
    Serial.println("CPS en este minuto"); 
    sendToSlaveC(R_CPS_NOW); // Solicitud I2C contador de segundos en ATtiny
    delay(10);

    requestFromSlave(); // Captura rta de Slave I2C
    filterValue(dataRequest); // Extrae el valor después de la coma
    Serial.print("----> CPS_NOW: ");
  }
  /* I2C CPS acumulados */
  else if(cmd == CPS_NOW_ACCUM){
    Serial.println("CPS acumulado actualmente"); 
    sendToSlaveC(R_CPS_NOW_ACUMM); // Solicitud I2C contador de segundos en ATtiny
    delay(10);

    requestFromSlave(); // Captura rta de Slave I2C
    filterValue(dataRequest); // Extrae el valor después de la coma
    Serial.print("----> CPS_NOW_ACUMM: ");
  }
  /* I2C segundos transcurridos */
  else if(cmd == TIME){
    Serial.println("tiempo trancurrido"); 
    sendToSlaveC(R_TIME); // Solicitud I2C contador de segundos en ATtiny
    delay(10);

    requestFromSlave(); // Captura rta de Slave I2C
    filterValue(dataRequest); // Extrae el valor después de la coma
    Serial.print("----> TIME (segundos): ");
  }
  /* I2C segundos transcurridos + CPS*/
  else if(cmd == CPS_TIME){
    Serial.println("tiempo trancurrido + CPS"); 
    sendToSlaveC(R_CPS_TIME); // Solicitud I2C contador de segundos en ATtiny
    delay(10);

    requestFromSlave(); // Captura rta de Slave I2C
    filterValue(dataRequest); // Extrae el valor después de la coma
     //// obs: se puede crear un filter parecido al de coma  para separar cps y time
    Serial.print("----> CPS_TIME: ");
  }

  /* I2C segundos transcurridos + CPM*/
  else if(cmd == CPM_TIME){
    Serial.println("tiempo trancurrido + CPM"); 
    sendToSlaveC(R_CPM_TIME); // Solicitud I2C contador de segundos en ATtiny
    delay(10);

    requestFromSlave(); // Captura rta de Slave I2C
    filterValue(dataRequest); // Extrae el valor después de la coma
     //// obs: se puede crear un filter parecido al de coma  para separar cps y time
    Serial.print("----> CPM_TIME: ");
  }
  
  Serial.println(dataRequest); // Envia por terminal
  sendToAppUart(dataRequest); // Envia a APP
}