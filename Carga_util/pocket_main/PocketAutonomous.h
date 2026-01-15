#ifndef POCKET_AUTONOMOUS_H
#define POCKET_AUTONOMOUS_H

#include <Arduino.h>
#include <Wire.h>

/**
 * @brief Módulo simplificado de adquisición autónoma de datos PocketCube
 * @details Adquisición automática cada 1 segundo, sin dependencias externas
 * @author Grupo SyCE - PocketCube
 */

// Constantes públicas
#define I2C_SLAVE_ADDR 0x08
#define MAX_DATA_I2C 33

#define STR_MEAS1 '1'

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
 * @details Configura I2C y timer para lecturas automáticas cada 1 segundo
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
 * @brief Inicia la adquisición automática de datos
 * @return void
 */
void pocketAutoStart();

/**
 * @brief Detiene la adquisición de datos
 * @return void
 */
void pocketAutoStop();

/**
 * @brief Obtiene el último dato recibido
 * @param buffer Buffer donde se guardará el dato (solo el valor, sin ID)
 * @param bufferSize Tamaño del buffer
 * @return Tamaño de datos copiados, 0 si no hay datos
 */
int pocketAutoGetData(char* buffer, int bufferSize);

/**
 * @brief Verifica si hay conexión con el esclavo I2C
 * @return true si conectado, false en caso contrario
 */
bool pocketAutoIsConnected();

#endif // POCKET_AUTONOMOUS_H
