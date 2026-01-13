#ifndef POCKET_AUTONOMOUS_H
#define POCKET_AUTONOMOUS_H

#include <Arduino.h>
#include <Wire.h>

/**
 * @brief Módulo autónomo de adquisición de datos PocketCube
 * @details No depende de una app externa. La adquisición es automática
 * @author Grupo SyCE - PocketCube
 */

// Constantes públicas
#define I2C_SLAVE_ADDR 0x08
#define MAX_DATA_I2C 33
#define MAX_SIZE_MEAS 7

#define STR_MEAS1 '1'

// Valores de sensores disponibles
#define SENSOR_MEAS1 1
#define SENSOR_STATE 6

/*** Macros de Tiempos Predefinidos (en segundos) ***/
#define TIME_10_SEC    10
#define TIME_30_SEC    30
#define TIME_1_MIN     60
#define TIME_2_MIN     120
#define TIME_5_MIN     300
#define TIME_10_MIN    600
#define TIME_15_MIN    900
#define TIME_30_MIN    1800
#define TIME_1_HOUR    3600
#define TIME_2_HOURS   7200
#define TIME_4_HOURS   14400
#define TIME_6_HOURS   21600
#define TIME_12_HOURS  43200
#define TIME_24_HOURS  86400

/**
 * @brief Inicializa el módulo autónomo
 * @details Configura I2C, Timer y comienza la adquisición automática
 * @return void
 */
void pocketAutoInit();

/**
 * @brief Actualiza el módulo - debe llamarse desde loop()
 * @details Procesa lecturas I2C automáticas
 * @return void
 */
void pocketAutoUpdate();

/**
 * @brief Inicia la adquisición de datos automática
 * @details El timer genera interrupciones periódicamente
 * @return void
 */
void pocketAutoStart();

/**
 * @brief Detiene la adquisición de datos
 * @details Desactiva el timer
 * @return void
 */
void pocketAutoStop();

/**
 * @brief Verifica si la adquisición está activa
 * @return true si está activa, false en caso contrario
 */
bool pocketAutoIsRunning();

/**
 * @brief Configura el intervalo de lectura en segundos
 * @param seconds Segundos entre lecturas (mínimo 1, máximo 255)
 * @return true si se configuró correctamente, false si el valor es inválido
 */
bool pocketAutoSetInterval(uint8_t seconds);

/**
 * @brief Obtiene el intervalo actual en segundos
 * @return Intervalo en segundos
 */
uint8_t pocketAutoGetInterval();

/**
 * @brief Obtiene la última lectura de datos
 * @param sensorId ID del sensor (SENSOR_MEAS1, SENSOR_STATE)
 * @param buffer Buffer donde se guardará el resultado
 * @param bufferSize Tamaño del buffer
 * @return Tamaño de datos copiados, 0 si no hay datos disponibles
 */
int pocketAutoGetLastReading(uint8_t sensorId, char* buffer, int bufferSize);

/**
 * @brief Define una función callback para ejecutar cuando hay nuevos datos
 * @details Se ejecuta cuando se recibe una lectura completa del esclavo
 * @param callback Función: void callback(int sensorId, const char* data)
 * @return void
 */
void pocketAutoSetDataCallback(void (*callback)(int, const char*));

/**
 * @brief Fuerza una lectura inmediata (no espera el timer)
 * @return void
 */
void pocketAutoReadNow();

/**
 * @brief Obtiene el estado de conexión con el esclavo I2C
 * @return true si hay comunicación, false en caso contrario
 */
bool pocketAutoIsConnected();

/**
 * @brief Reinicia la comunicación I2C
 * @return void
 */
void pocketAutoResetConnection();

#endif // POCKET_AUTONOMOUS_H
