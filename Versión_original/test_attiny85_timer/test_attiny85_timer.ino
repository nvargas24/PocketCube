#include <avr/interrupt.h>
#include <avr/io.h>

volatile uint16_t pulseCount = 0; // Contador de pulsos

void setup() {
  // Configura el pin PB0 como salida (LED)
  pinMode(0, OUTPUT);
  
  // Configura el pin PB3 como entrada
  pinMode(3, INPUT);
  
  // Configura la interrupción externa en el pin PB3 (INT0)
  GIMSK |= (1 << INT0);        // Habilita la interrupción externa INT0
  MCUCR |= (1 << ISC01) | (1 << ISC00); // Configura la interrupción para flanco ascendente
  
  // Habilita interrupciones globales
  sei();
}

void loop() {
  // Enciende y apaga el LED cada segundo
  digitalWrite(0, HIGH); // Enciende el LED
  delay(1000);
  digitalWrite(0, LOW);  // Apaga el LED
  delay(1000);
}

// Manejador de interrupción para contar los pulsos
ISR(INT0_vect) {
  pulseCount++; // Incrementa el contador de pulsos
}
