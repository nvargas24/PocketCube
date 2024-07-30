void OprBot()
{
  heartbeat();

  rf22.setModeIdle();
  
    
  sendmsg ("CQ CQ CQ DE ");
  sendmsg (SDR);
  sendmsg (" AR");
    
  unsigned long str = millis();

  
while ((millis()-str) <= 20000)

{
  
    Robot ();

//Serial.println(flg1);

if (flg1 == true){ break;}

  }

 // Serial.println(F("OUT RBT"));
  
   X.trim();
   
  //Serial.println(X);

  char U[8]= "";
  
  X.toCharArray(U, (X , X.length()+1));

  for ( _V = 0; _V <= X.length(); _V++)
  {
  //Serial.println(U[_V]);
  
   if ((U [_V]) == ' ')
   {
  
    break;
  }
  
  }

//Serial.println(X.substring(0 , _V));

if ( X.substring(0 , _V) == ID2 && X.endsWith("AR"))

{

//Serial.println(X.length()); //largo del frame de cw 
  
  if (ID2.length() == 6 && X.length() == 18)
  {
    X.substring(10,15).toCharArray(Z,(X.substring(10,15)).length()+1);

 //   Serial.println(X.substring(10,15));
    
    }
    
 if (ID2.length() == 6 &&  X.length() == 19)
 {
  X.substring(10,16).toCharArray(Z,(X.substring(10,16)).length()+1);
  //Serial.println(X.substring(10,16));
 }
 
 if (ID2.length() == 5 && X.length() == 18)
 {
  X.substring(15,9).toCharArray(Z,(X.substring(15,9)).length()+1);
 // Serial.println(X.substring(15,9));
  }

 if (ID2.length() == 5 && X.length() == 17)
{
  X.substring(14,9).toCharArray(Z,(X.substring(14,9)).length()+1);
 // Serial.println(X.substring(14,9));
    
  }

 if (ID2.length() == 4 && X.length() == 17)
{
  X.substring(14,8).toCharArray(Z,(X.substring(14,8)).length()+1);
  // Serial.println(X.substring(14,8));
}

if (ID2.length() == 4 && X.length() == 16)

{
  X.substring(13,8).toCharArray(Z,(X.substring(13,8)).length()+1);
 // Serial.println(X.substring(13,8));
}

 QSL = QSL + 1;

EEPROM.write(12, QSL );

QSO = QSO + 1;


    n = sprintf(Q,"%d",QSL);
    strcat (T , Z);
    strcat(T,",");
         
    sendmsg ("V V V ");
    
    sendmsg (Z) ;//seÃ±al distintiva del operador
    
    sendmsg ("DE ");
    
    sendmsg (SDR);//señal distintiva del robot
    
    sendmsg (" QSO NR ");

    sendmsg (Q);

    sendmsg (" OP ROBOT 73 SK");
   
   }
      
  n = sprintf(superbuffer,"%s",T);

  int ll = strlen (superbuffer);

   EEPROM.write(15,ll);

   for(int vv = 0; vv <= ll; vv++)
   {
  EEPROM.write(100+vv, superbuffer[vv]);
  
   }

   EEPROM.write(16,1);
   
    heartbeat();
    
    if (QSO >= CALL )
{
  EEPROM.write(4, 0);

  //EEPROM.write(16,1);
  
  bitWrite(_status,3,0);//APAGO EL ROBOT

_FR = 1;
  
 bitWrite(_status,1,1);//AVISO EL LOG ESTA LLENO
  
/*
  _FR = 1;
  
 bitWrite(_status,1,1);
  
  n = sprintf(superbuffer,"%s",T);

  int ll = strlen (superbuffer);

   EEPROM.write(15,ll);

   for(int vv = 0; vv <= ll; vv++)
   {
  EEPROM.write(100+vv, superbuffer[vv]);
  
   }
   */
      memset(superbuffer, 0, sizeof(superbuffer));

      char T[]="";
  /*    
      for (int jj = 0; jj <= ll; jj++)
      
      {
        Serial.println (char (EEPROM.read(100+jj)));
        }
        */
}
  
    X="";
    j=0;
    
    LowPower.powerDown(SLEEP_8S, ADC_OFF, BOD_OFF);
    LowPower.powerDown(SLEEP_2S, ADC_OFF, BOD_OFF);
    LowPower.powerDown(SLEEP_2S, ADC_OFF, BOD_OFF);
    LowPower.powerDown(SLEEP_2S, ADC_OFF, BOD_OFF);
    LowPower.powerDown(SLEEP_1S, ADC_OFF, BOD_OFF);

 }
