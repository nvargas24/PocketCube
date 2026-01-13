/**
 * @file pocket_autonomous_example.ino
 * @brief Ejemplo de uso del módulo autónomo PocketAutonomous
 * @details Adquisición automática de datos sin dependencia de app externa
 * @author Grupo SyCE - PocketCube
 */

#include <Wire.h>
#include "PocketAutonomous.h"

// Variables globales
// NOTA: DISPLAY_INTERVAL removido - sincronización automática con callback

/**
 * @brief Callback ejecutado cuando hay nuevos datos disponibles
 * También muestra el estado del sistema (opción híbrida)
 */
void onNewData(int sensorId, const char* data)
{
  // Mostrar datos de lectura
  Serial.println("\n════════════════════════════════════════════════════════════════════════════");
  Serial.print("📊 LECTURA #");
  static unsigned long readCount = 0;
  Serial.println(++readCount);
  Serial.print("Sensor ID: ");
  Serial.println(sensorId);
  Serial.print("Valor: ");
  Serial.println(data);
  
  // Mostrar estado del sistema
  printStatus();
  Serial.println("════════════════════════════════════════════════════════════════════════════\n");
}

/**
 * @brief Muestra el estado actual del sistema
 */
void printStatus()
{
  Serial.print("Estado: ");
  if(pocketAutoIsRunning()){
    Serial.print("▶ CORRIENDO");
  } else {
    Serial.print("⏸ PAUSADO");
  }
  
  Serial.print(" | Conectado: ");
  if(pocketAutoIsConnected()){
    Serial.print("✓ SÍ");
  } else {
    Serial.print("✗ NO");
  }
  
  Serial.print(" | Intervalo: ");
  Serial.print(pocketAutoGetInterval());
  Serial.println(" seg");
}

/**
 * @brief Configuración inicial
 */
void setup() 
{
  // Inicializar comunicaciones
  Serial.begin(9600);
  Wire.begin();
  
  Serial.println("=== PocketCube - Módulo Autónomo ===");
  delay(500);
  
  // Inicializar módulo (comienza automáticamente la adquisición)
  pocketAutoInit();
  
  // Registrar callback para nuevos datos
  pocketAutoSetDataCallback(onNewData);
  
  // Configurar intervalo de lectura (usando macro de tiempo)
  // 1 minuto entre lecturas
  pocketAutoSetInterval(TIME_1_MIN);
  
  Serial.println("✓ Módulo iniciado");
  Serial.println("✓ Adquisición automática activada");
  Serial.print("✓ Intervalo de lectura: ");
  Serial.print(pocketAutoGetInterval());
  Serial.println(" segundos (1 minuto)");
  Serial.println("\n✓ Sistema listo - Esperando primera lectura...");
  Serial.println();
}

/**
 * @brief Bucle principal
 */
void loop() 
{
  // Actualizar el módulo autónomo (CRÍTICO)
  pocketAutoUpdate();
  
  // Procesar comandos desde serial
  serialCommandHandler();
  
  // Pequeño delay para evitar saturar el procesador
  delay(50);
}

/**
 * @brief Procesa comandos desde puerto serial
 * @details Comandos disponibles:
 *   - "START"        : Inicia la adquisición
 *   - "STOP"         : Detiene la adquisición
 *   - "READ"         : Fuerza una lectura inmediata
 *   - "INFO"         : Muestra información del módulo
 *   - "INTERVAL [n]" : Establece intervalo a n segundos
 *   - "RESET"        : Reinicia la conexión I2C
 */
void serialCommandHandler()
{
  if(Serial.available()){
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();
    cmd.toUpperCase();
    
    if(cmd == "START"){
      pocketAutoStart();
      Serial.println("✓ Adquisición iniciada");
    }
    else if(cmd == "STOP"){
      pocketAutoStop();
      Serial.println("✓ Adquisición detenida");
    }
    else if(cmd == "READ"){
      pocketAutoReadNow();
      Serial.println("✓ Lectura inmediata solicitada");
    }
    else if(cmd == "INFO"){
      Serial.println("\n=== INFORMACIÓN DEL MÓDULO ===");
      Serial.print("Estado: ");
      Serial.println(pocketAutoIsRunning() ? "CORRIENDO" : "PAUSADO");
      Serial.print("Conectado: ");
      Serial.println(pocketAutoIsConnected() ? "SÍ" : "NO");
      Serial.print("Intervalo: ");
      Serial.print(pocketAutoGetInterval());
      Serial.println(" segundos");
      Serial.println();
    }
    else if(cmd.startsWith("INTERVAL ")){
      int spaceIndex = cmd.indexOf(' ');
      String numStr = cmd.substring(spaceIndex + 1);
      int newInterval = numStr.toInt();
      
      if(pocketAutoSetInterval(newInterval)){
        Serial.print("✓ Intervalo establecido a ");
        Serial.print(newInterval);
        Serial.println(" segundos");
      } else {
        Serial.println("✗ Error: intervalo inválido (1-255)");
      }
    }
    else if(cmd == "RESET"){
      Serial.println("Reiniciando conexión I2C...");
      pocketAutoResetConnection();
      if(pocketAutoIsConnected()){
        Serial.println("✓ Conexión restaurada");
      } else {
        Serial.println("✗ Error: No se puede conectar con el esclavo");
      }
    }
    else if(cmd != ""){
      Serial.println("Comandos disponibles:");
      Serial.println("  START       - Inicia adquisición");
      Serial.println("  STOP        - Detiene adquisición");
      Serial.println("  READ        - Lectura inmediata");
      Serial.println("  INFO        - Información del módulo");
      Serial.println("  INTERVAL n  - Establece intervalo (segundos)");
      Serial.println("  RESET       - Reinicia conexión I2C");
    }
  }
}
