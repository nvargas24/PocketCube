void setup() {

  
 

}

void loop() {




  
  PORTB |= (1 << PORTB1);//Enciende el led
delay(1000);
// set PB6 low
  PORTB &= ~(1 << PORTB1);//Apaga el led
 delay(1000);
  delay (20);
}
