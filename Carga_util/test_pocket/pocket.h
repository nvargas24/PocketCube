#ifndef TEST_POCKET_H
#define TEST_POCKET_H

#include <Wire.h>
#include <Arduino.h>

/*********************** Macros *********************/
#define I2C_SLAVE_ADDR 0x08
#define MAX_DATA_I2C 33

#define SEND_LINE_APP 7
#define SEND_CPS_APP 8
#define SEND_CPM_APP 9

#define NO_CMD 0
#define CMD_I2C 1

#define CPM 1
#define CPS_NOW 2
#define TIME 3
#define CPS_NOW_ACCUM 4
#define CPS_TIME 5
#define CPM_TIME 6

#define R_CPM '1'
#define R_CPS_NOW '2'
#define R_TIME '3'
#define R_CPS_NOW_ACUMM '4'
#define R_CPS_TIME '5'
#define R_CPM_TIME '6'

/****************** Variables globales ***************/ 
/* I2C */
extern char dataRequest[MAX_DATA_I2C]; // Str respuesta de Slave

/* UART */
extern int serial_id;
extern int value;

/********* Declaracion de funciones *********/
void filterValue(char *);

/* I2C */
void sendToSlaveC(char);
int requestFromSlave();
void requestI2C(const uint8_t);

/* UART */
void requestFromAppUart(int*, int*);
void sendToAppUart(const char*);

#endif