void dash()
{
//  digitalWrite(LEDpin, HIGH) ;
  rf22.spiWrite(0x07, 0x08); // turn tx on
  delay(DASHLEN);
//digitalWrite(LEDpin, LOW) ;
  rf22.spiWrite(0x07, 0x01); // turn tx off
  delay(DOTLEN) ;
}

void dit()
{
  //digitalWrite(LEDpin, HIGH) ;
  rf22.spiWrite(0x07, 0x08); // turn tx on
  delay(DOTLEN);
  rf22.spiWrite(0x07, 0x01); // turn tx off
//digitalWrite(LEDpin, LOW) ;
  delay(DOTLEN);
}

void send(char c)
{
  int i ;
  if (c == ' ') 
  {
   // Serial.print(c) ;
    delay(7*DOTLEN) ;
    return ;
  }
  for (i=0; i<N_MORSE; i++)
  {
    if (morsetab[i].c == c) 
    {
      unsigned char p = morsetab[i].pat ;
      //Serial.print(morsetab[i].c) ;

      while (p != 1)
      {
          if (p & 1)
            dash() ;
          else
            dit() ;
          p = p / 2 ;
      }
      delay(2*DOTLEN) ;
      return ;
    }
  }
  /* if we drop off the end, then we send a space */
 // Serial.print("?") ;
}
