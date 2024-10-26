#include <Wire.h>

void setup() {
  Serial.begin(9600); // Inicializa la comunicación serial
  Wire.begin(); // Inicia la comunicación I2C como maestro
}

void loop() {
  Wire.requestFrom(8, 1); // Solicita 16 bytes al esclavo con dirección 8
  while (Wire.available()) { // Mientras haya datos disponibles
    char c = Wire.read(); // Lee un byte
    Serial.print(c); // Imprime el byte en el monitor serial
  }
  Serial.println(); // Nueva línea
  delay(1000); // Espera un segundo
}
