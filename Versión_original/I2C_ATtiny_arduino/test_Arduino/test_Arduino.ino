#include <Wire.h>

void setup() {
  Serial.begin(9600); // Inicializa la comunicación serial
  Wire.begin(); // Inicia la comunicación I2C como maestro
}

void loop() {
  const int maxBytes = 33; // Máximo de bytes a recibir
  char dataRequest[maxBytes + 1]; // Array para almacenar el mensaje (33 + 1 para el carácter nulo)

  uint8_t index = 0;  
  char receivedChar;
  int size_rta = 0;

  // Datos a enviar al esclavo
  char data = '1'; // Solo se envía el carácter "1"

  /* Envio datos I2C */
  Wire.beginTransmission(8); // Comienza la transmisión hacia el esclavo con dirección 8
  Wire.write(data); // Envía el carácter "1"
  Wire.endTransmission(); // Finaliza la transmisión

  delay(100); // Pequeña espera para asegurar que el esclavo reciba el dato

  /* Preparo Master para recibir respuesta de Slave  */
  Wire.requestFrom(8, sizeof(dataRequest)); // Solicitud a slave

  // Leer datos enviados por el esclavo
  while (Wire.available() && (index < maxBytes)) {
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

  /* Verifico datos recibidos*/
  Serial.print("R-Slave: ");
  Serial.println(dataRequest);
  delay(1000); // Espera un segundo
}
