//
// VERSION 09-04-2020
//
//SALTEA LA RECEPCION CUANDO EL LOGGER ESTA ACTIVO
//CARGA CALLSIGN DE LA BALIZA EN FORMA REMOTA
//CARGA CALLSIGN DEL ROBOT EN FORMA REMOTA
//SE AGREGA COMANDO *C PARA LIMPIAR RELAY MSG
//SE AGREGA COMANDO *K APAGA ROBOT
//SE CAMBIA A3 COMO SALIDA DIGITAL PARA CONTROLAR MPPT
// A1 SENSA CORRIENTE DE CARGA
//A2 SENSA CORRIENTE DE CONSUMO DE LA PLACA ARDUINO
//
//RTTY A 100_BD 7 BITS N 2 STOP SHIFT 470 HZ
//
/*
 * LISTA DE 15 COMANDOS KONDOR
 * 
 *1  *0 =RESET PROGRAMA
 -2  *1 =CAMBIA POTENCIA Y STATUS
 -3  *2 =CAMBIA A LW2DTZ,STATUS Y POTENCIA
 -4  *3 =CAMBIA CALLSIGN DIY1
 -5  *4 =CAMBIA SEÃ‘AL ID EJ *4LU1XXX o LU1XX
 -6  *5 =CAMBIA POTENCIA MAXIMA DE SALIDA 
 -7  *R =ACTIVA ROBOT
 -8  *W =WRITE LOGGER
 -9  *D =DOWNLOAD LOGGER
 -10 *T =THHMMSSDDMMAAAA EJ *T21100020012020
 -11 *B =RELAY MENSAJE DE 30 CARACTERES EJ *B HIHIHI
 -12 *L =ENCIENDE EL LED 1 SEGUNDO
 -13 *K =APAGA ROBOT
 -14 *C =LIMPIA EL RELAY MENSAJE
 -15 *S =SAVE BATERIA
 -16 *N =MODO NORMAL
 * 
 *  MEMORIA EEPROM 24LC32 DE 4KB o 64 PAGINAS DE 64 BYTES
 *   
 */
#include "settings.h"

/*
 0x01  1db (1mW) 
 0x02  5db (3mW)
 0x03  8db (6mW)
 0x04 11db (12mW)
 0x05 14db (25mW)
 0x06 17db (50mW)
 0x07 20db (100mW)
 */

#include <SPI.h>
#include <RF22.h>
#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include "LowPower.h"
#include <Wire.h>
#include <EEPROM.h>
#include <virtuabotixRTC.h>

#include <Vcc.h>

Vcc vcc(VccCorrection);

RF22 rf22;

//RTTY A 100BD 7 BITS N 2 STOP

uint8_t buf [RF22_MAX_MESSAGE_LEN];

virtuabotixRTC myRTC(8, 7, 6);

RF22::ModemConfig FSK_500bd =  { 0x2b, 0x03, 0xd0, 0xe0, 0x10, 0x62,0x00, 0x05, 0x40, 0x0a, 0x1d, 0x80, 0x60, 0x04, 0x19, 0x2c, 0x22,0x08 };// these values correspond to 500bps tx rate no manchestger FSK - and are the lowest values that are


 /*
void Bat_Mon()
{
  for (int i=0; i <= 10; i++)
{
  float v = vcc.Read_Volts();
  
battVolts = int (v * 100);

    }

}
*/


// RTTY Functions - from RJHARRISON's AVR Code


void rtty_txstring (char * string)
{
 
	/* Simple function to sent a char at a time to 
	** rtty_txbyte function. 
	** NB Each char is one byte (8 Bits)
	*/
	char c;

	c = *string++;
	while ( c != '\0')
	{
		rtty_txbyte (c);
		c = *string++;
  }
}
 
void rtty_txbyte (char c)
{
	/* Simple function to sent each bit of a char to 
	** rtty_txbit function. 
	** NB The bits are sent Least Significant Bit first
	**
	** All chars should be preceded with a 0 and 
	** proceded with a 1. 0 = Start bit; 1 = Stop bit
	**
	** ASCII_BIT = 7 or 8 for ASCII-7 / ASCII-8
	*/
	int i;
	rtty_txbit (0); // Start bit
	// Send bits for for char LSB first	
	for (i=0;i<7;i++)
	{
		if (c & 1) rtty_txbit(1); 
			else rtty_txbit(0);	
		c = c >> 1;
	}
	rtty_txbit (1); // Stop bit
        rtty_txbit (1); // Stop bit
      
        
}
 
 
// FSK is accomplished by twiddling the frequency offset register. This gives us approx 315Hz shift. 

void rtty_txbit (int bit)
{
		if (bit)
		{
		  // high
               
                  rf22.spiWrite(0x073, 0x03);
		}
		else
		{
		  // low
               
                  rf22.spiWrite(0x073, 0x00);
		}
              delayMicroseconds(9750);// 100 baud x 8MHZ
           //delayMicroseconds(19500);// 50 baud x 8MHZ
 	       //  delayMicroseconds(3400);// 300 baud X 8MHZ
        //delayMicroseconds(750);// 150 baud X 1MHZ
        //delayMicroseconds(2500);// 50 baud X 1MHZ
 
}



void RFM22B_RTTY_Mode()
{
	rf22.setFrequency(TX_FREQ);
	rf22.setModeTx();
	rf22.setModemConfig(RF22::UnmodulatedCarrier);
	rf22.spiWrite(0x073, 0x03); // Make sure we're on the high tone when we start
  digitalWrite (A3,LOW);//APAGA EL MPPT ENCIENDE EL OPTO

      delay(10);
                       
  
  analogReference(INTERNAL);
  delay (10);
  for (int lap =0; lap<=2; lap = lap +1)
       {    
     
      CTx = (analogRead(A2)/8)-7;//CORRIENTE QUE CONSUME EL TRANSMISOR SIN MPPT menos lo que consume el led del opto -7 mA
      CTx = constrain(CTx, 0, 150);
      delay (10);
       }
  
  analogReference(DEFAULT);
  delay(10);
  digitalWrite (A3,HIGH);//ENCIENDE EL MPPT APAGA EL OPTO
  
	}

////////////////////////////////////////////////////////////////////////////////////

void setup()
{
   Serial.begin(9600);
   
if (MCUSR & _BV(EXTRF))
{
     // Reset button or otherwise some software reset
    // Serial.println("Reset button was pressed.");
      _RSC = EEPROM.read(7);

         _RSC = _RSC + 1 ;
   
        EEPROM.write(7, _RSC);

       // Serial.print("RST = ");
    
       // Serial.println(_RSC);
    
        QSL = EEPROM.read(12);
        
    MCUSR = 0;
        
if (EEPROM.read(20) == 1)
{
  bitWrite(_status,4,1);
  }

if (EEPROM.read(16) == 1)
{
  bitWrite(_status,1,1);

  _FR = EEPROM.read(16);
  }
}
 
 if (MCUSR & (_BV(BORF) | _BV(PORF)))
 {
      // Brownout or Power On
   // Serial.println("Power loss occured!");
    _RSC = 0;
    QSL = 0;
    EEPROM.write(2, 0);
    EEPROM.write(7, 0);
    EEPROM.write(9, 0);//ACTIVA BALIZA CW
    EEPROM.write(11, 0);//LOG ROBOT LISTO
    EEPROM.write(12, QSL);
    EEPROM.write(16,0);
    EEPROM.write(20,0);//LOGGER VACIO

    
    bitWrite(_status,0,0);
    bitWrite(_status,1,0);
    bitWrite(_status,2,0);
    bitWrite(_status,3,0);
    bitWrite(_status,4,0);
    bitWrite(_status,5,0);
    bitWrite(_status,6,0);
    bitWrite(_status,7,0);
        
    MCUSR = 0;

    bitWrite(_status,5,1);
 }

pinMode (A3, OUTPUT);// LOW APAGA EL MPPT

digitalWrite (A3,HIGH);//HIGH ENCIENDE EL MPPT


myRTC.setDS1302Time(00, 00, 00, 6, 01, 01, 2020);

EEPROM.write(addr, 0);

EEPROM.write(1, 0);

EEPROM.write(3, 0);
EEPROM.write(4, 0);// ROBOT
EEPROM.write(5, 0);
EEPROM.write(6, 0);//POWER SAVE BATERIA


if (rf22.init())
{
Serial.println(F("RF22 init OK"));
rf22.setFrequency(TX_FREQ , 0.00);

} 
else
{
Serial.println(F("RF22 init FAILED"));
} 

// end if you will probably need to change this to correct for crystal error
/*
 0x02  5db (3mW)
 0x03  8db (6mW)
 0x04 11db (12mW)
 0x05 14db (25mW)
 0x06 17db (50mW)
 0x07 20db (100mW)
 */
rf22.spiWrite(0x6d,RADIO_POWER );    //  25 mW
rf22.spiWrite(0x09, 202);//ajuste fino de la frecuencia
rf22.spiWrite(0x01C, 0x29);     //IF Filter Bandwidth
rf22.spiWrite(0x02A, 0x08);   // Set the AFC register to allow +- (0x08 * 625Hz) pull-in (~+-5KHz)

    rf22.spiWrite(0x1D, 0x40);
    rf22.spiWrite(0x30, 0x8C);
    rf22.spiWrite(0x32, 0x8C);
    rf22.spiWrite(0x33, 0x42);

   rf22.spiWrite(0x34, 0x10);

    rf22.spiWrite(0x35, 0x22);
    
    rf22.spiWrite(0x03A, 36);
    rf22.spiWrite(0x03B, 53);

    rf22.spiWrite(0x3F, 36);
    rf22.spiWrite(0x40, 53);

    

  rf22.setModemConfig(RF22::UnmodulatedCarrier);

  rf22.setModeIdle();

  resetInputSignal();           // Reset input signal buffer
 
  X="";
  j=0;
  QSO = 0;

ID.toCharArray(Input,7);

 do {
   currentMillis = millis();
} while ( currentMillis < 60000 );

}

/////////////////////////////////////////////////////////

void loop()
{
    
   myRTC.updateTime();
   
  //Serial.println(F("INICIO v04.07.2020.2"));

  analogReference(INTERNAL);

  delay(10);
  
   CBat  = (analogRead(A1)/8);//CORRIENTE QUE ENTREGA EL MPPT A LA BATERIA

   CBat = constrain(CBat, 0, 100);
        
   delay (10);
  
  // Serial.println(CBat);
  
///////////////////////////////////////////////////////////////////

    digitalWrite (A3,LOW);//APAGA EL MPPT

    delay(10);
      
      
      CBor  = ((analogRead(A2)/8)-7);//CORRIENTE QUE CONSUME LA PLACA SIN MPPT, (LOS 7 mA son del OPTOAISLADOR)
     
      CBor = constrain(CBor, 0, 100);


     delay (10);
              
      analogReference(DEFAULT);
      
      delay (10);


      digitalWrite (A3,HIGH);// ENCIENDE EL MPPT

      delay (10);
        
heartbeat();

//------------------------------------------------------------------------
      float v = vcc.Read_Volts();

      battVolts = int ((v +0.15)* 100);// TENSION DE LA BATERIA CON MPPT ACTIVO

if (battVolts <= 370)
{
    rf22.spiWrite(0x6d,RADIO_POWER );    //  25 mW
    delay (5);
    bitWrite(_status,5,1);
    EEPROM.write(addr, 0);
  }
            
     // Serial.println(battVolts);
        
   value = EEPROM.read(3);/////DIRECCION EEPROM 3 DEL AT328P

   delay (5);

     if (value == 1)
     {
      logger_out();
     }
         
  value = EEPROM.read(address);/////DIRECCION EEPROM 0 DEL AT328P
  
 if (value == 2 )
  {
       rf22.setTxPower(RF22_TXPOW_17DBM);       
       bitWrite(_status,0,1);
       
      
    }

   if (value == 5 )
   {
     rf22.setTxPower(RF22_TXPOW_20DBM);
     
     bitWrite(_status,0,0); 
     
    }

 if (value == 3)
  {
 ID = "DIY1";
 ID.toCharArray(Input,5);

   }

  
value = EEPROM.read(4);

  if ((value == 1) && (bitRead(_status,2) == 1))
  {
   
flg1=false;

bitWrite(_status,3,1);

OprBot();


rf22.setModeIdle();


   }
 

value = EEPROM.read(1);//DIRECCION 1 DE LA EEPROM DEL AT328P
 
if (value == 1)
{

  EEPROM.write(1,0);
  delay(5);
  
  memset (RM, 0, sizeof(30));//reset del array
  for (int lc = 0; lc < 29 ; lc += 1)
 {
RM [lc] = 0;

}

 EEPROM.write(1,1);
 delay(5);

}

//CAMBIO DE SEÑAL DISTINTIVA BALIZA *1

value = EEPROM.read(addr);//DIRECCION 1 DE LA EEPROM DEL AT328P

if (value == 1)
{
  ID = command.substring(2,command.length());// cambia señal distintiva del beacon de de rtty
  ID.toCharArray(Input,ID.length()+1);
  EEPROM.write(addr,0);

}

//SETEO SEÑAL DISTINTIVA ROBOT *4xxxxxx

value = EEPROM.read(5);

if (value == 1)
{
  ID2 = "";
  
  ID2 = command.substring(2,(command.length()));
  
  ID2.trim();

  //Serial.println(ID2);
  
  EEPROM.write(5,0);

  bitWrite(_status,2,1);

  char SDR[] = "";

}


ID2.toCharArray(SDR,(ID2.length()+1));
 
float voltage= battVolts;

dtostrf(voltage, 3, 0, cadenaTemporal_3);

if (_SMeter == true)
{
rssi_floor = ((int)rf22.lastRssi()*51 - 12400)/100; // Linear approximation to the graph in the datasheet.
_SMeter = false;
}

else {
  rssi_floor = ((int)rf22.rssiRead()*51 - 12400)/100;
}

dtostrf(rssi_floor,3, 0, cadenaTemporal_1);

t_cpu = (GetTemp()*10);//temperatura del cpu

t_cpu = constrain(t_cpu, 0, 900);
/*
Serial.print(F("TEMP= "));

Serial.println(t_cpu);

Serial.println(rf22.spiRead(0x09));

Serial.println(rf22.spiRead(0x3A));
Serial.println(rf22.spiRead(0x3B));
Serial.println(rf22.spiRead(0x1D));
Serial.println(" ");
Serial.println(rf22.spiRead(0x75));
Serial.println(rf22.spiRead(0x76));
Serial.println(rf22.spiRead(0x77));
*/

dtostrf(t_cpu, 3, 0, cadenaTemporal);

int rfm_temp = (rf22.temperatureRead( RF22_TSRANGE_M64_64C,-28 ) / 2) - 64;

    value = EEPROM.read(2);/////DIRECCION EEPROM 2 DEL AT328P

    delay (5);

     if (value == 1)
     {
      logger_in();
     }

if (battVolts >= 360 && value == 0 )//ESTA EL LOGGER ACTIVO ? == 0 NO / == 1 SI
{


n = sprintf(txbuffer, "$%02d%02d%02d,%02d,%02d,%02d,%03d,%s,%s,%d,%s,%0d,%02X*\n",myRTC.hours,myRTC.minutes,myRTC.seconds,CBat,CBor,CRx,CTx,cadenaTemporal_3,cadenaTemporal_1,rfm_temp,cadenaTemporal,_RSC,_status);

n = sprintf(superbuffer,"%s",txbuffer);

rf22.setModemRegisters(&FSK_500bd);

process_data(superbuffer);

memset(superbuffer, 0, sizeof(superbuffer));

rf22.setModeIdle();


int _lz = (405 - battVolts) ;

_lz = constrain(_lz , 0, 44);

for (int _lv = 0; _lv <= _lz; _lv++)
{
  LowPower.powerDown(SLEEP_2S, ADC_OFF, BOD_OFF);
  
    }
    
  heartbeat();

  LowPower.powerDown(SLEEP_8S, ADC_OFF, BOD_OFF);
  LowPower.powerDown(SLEEP_2S, ADC_OFF, BOD_OFF);
 
  
int CW =EEPROM.read(9);

if ( CW == 1)
{
    
  rf22.setModemConfig(RF22::UnmodulatedCarrier);
  rf22.spiWrite(0x073, 0x03); // Make sure we're on the high tone when we start
  sprintf (txbuffer, "KA LW2DTZ %sV %sC",cadenaTemporal_3,cadenaTemporal);
  sprintf(superbuffer,"%s\n",txbuffer);
  sendmsg (superbuffer);
  memset(superbuffer, 0, sizeof(superbuffer));
}

if (CW ==0 )
{
n = sprintf(txbuffer, "$$$%s,%02d%02d%02d,%02d,%02d,%03d,%02d,%s,%s,%d,%s,%02X,%d,%s,%s*",Input,myRTC.hours,myRTC.minutes,myRTC.seconds,CBat,CBor,CTx,CRx,cadenaTemporal_3,cadenaTemporal_1,rfm_temp,cadenaTemporal,_status,_RSC,RM,Z);

  for (XOR = 0, i = 0; i <= strlen(txbuffer)+1; i++)
  {
    
   c = (unsigned char)txbuffer[i];
   if (c == '*') break;
   if (c != '$') XOR ^= c;
   }


n = sprintf(superbuffer,"%s%02X\n",txbuffer,XOR);

heartbeat();

//////////////////////////////////////////////////////////////////////////////////////////////
RFM22B_RTTY_Mode();

delay(10);

rtty_txstring ("RYRYRYRYRYRYRYRYRY");  
rtty_txstring (superbuffer);
memset(superbuffer, 0, sizeof(superbuffer));
delay(10);
    }

if(EEPROM.read(11) == 1)
{

delay (500);

int ll = EEPROM.read(15);

for (int pp = 0; pp <= ll; pp++)

{
  T[pp]= EEPROM.read(100+pp);
}

n = sprintf(superbuffer,"%s",T);

rtty_txstring ("RYRYRYRYRYRYRY CW LOG: ");

rtty_txstring (superbuffer);

memset(superbuffer, 0, sizeof(superbuffer));

EEPROM.write(11,0);

memset (T, 0, sizeof(70));

      }
  
  
heartbeat();

value = EEPROM.read(2);/////DIRECCION EEPROM 2 DEL AT328P ve si esta activo el logger

if( value !=1)
{
// RECEPCION DE DATOS 

  rf22.setModeRx();
  
  delay(2);

  digitalWrite (A3,LOW);//APAGA EL MPPT

      delay(10);

  analogReference(INTERNAL);

  delay(10);

     CRx= (((analogRead(A2)/8)-CBor)-7);//CORRIENTE QUE CONSUME EL RECEPTOR SIN MPPT op esta encendido


  CRx = constrain(CRx, 0, 100);
   
   delay (10);

   analogReference(DEFAULT);
   delay (10);
   digitalWrite (A3,HIGH);//ENCIENDE EL MPPT
   delay(5);
  rf22.setModemRegisters(&FSK_500bd);
  delay (2);

//Serial.println(F("RECEPCION"));

//memset(buf, 0, sizeof(RF22_MAX_MESSAGE_LEN));//reset del array//

  command ="";

    bitWrite(_status,7,0);

  if(rf22.waitAvailableTimeout(5000))
    {
    
      uint8_t buf[RF22_MAX_MESSAGE_LEN];
      
      uint8_t len = sizeof(buf);
      
      if (rf22.recv(buf, &len))
 {
command = (String((char*)buf)); 

command.trim();

_SMeter = false;

if (command !="")
{

_SMeter = true;

if (command.substring(0,2) == "*1")

{
  EEPROM.write(addr, 1);
  delay (10);
  bitWrite(_status,7,1);

}

 if (command.substring(0,2) == "*0")
{
 asm volatile ("  jmp 0");  
}

 if (command.substring(0,2) == "*2")
{
  EEPROM.write(addr, 2);
  delay (5);
  bitWrite(_status,5,0);
  bitWrite(_status,7,1);

}

 if (command.substring(0,2) == "*3")
{
  EEPROM.write(addr, 3);
  delay (5);
  bitWrite(_status,7,1);

}


 if (command.substring(0,2) == "*4")
{
 EEPROM.write(5, 1);
 delay (5);
 bitWrite(_status,7,1);
}

 if (command.substring(0,2) == "*5" && battVolts >= 380 )
{
 EEPROM.write(addr, 5);
 delay (5);
 bitWrite(_status,5,0);
 bitWrite(_status,7,1);

 
}

 if (command.substring(0,2) == "*R" && battVolts >= 380  )//ACTIVA ROBOT
{
  EEPROM.write (4, 1);
  delay (5);
  bitWrite(_status,1,0);
  bitWrite(_status,7,1);
  _FR = 0;
  EEPROM.write(16,0);
  
  memset (RM, 0, sizeof(30));//reset del array
   
   if (QSO >= CALL)
   {
   memset (T, 0, sizeof(70));
   QSO = 0;
   bitWrite(_status,1,0);
      
   }
}

 if (command.substring(0,2) == "*K")//APAGA ROBOT
{
  EEPROM.write(4, 0);
  delay (5);
  bitWrite(_status,3,0);
  bitWrite(_status,7,1);

}

 if (command.substring(0,2) == "*Q" && _FR == 1)
{
  EEPROM.write(11,1);

  bitWrite(_status,7,1);
 
  }

 if (command.substring(0,2) == "*W")
{
    //Serial.println(command.substring(0,2));

    
     _EEx = 0;
     
     //Serial.print ("EEx= ");
     
     //Serial.println (_EEx);
    
    EEPROM.write(2,1);
    
    delay(5);
       
    bitWrite(_status,7,1);

}

if (command.substring(0,2) == "*D")
{
  EEPROM.write(3, 1);
  delay (10);
  bitWrite(_status,7,1);

}

else if (command.substring(0,2) == "*L")
{

//set PB1 high
  PORTB |= (1 << PORTB1);//Enciende el led
  delay(1000);
// set PB1 low
  PORTB &= ~(1 << PORTB1);//Apaga el led
}

else if (command.substring(0,2) == "*C")
{
  EEPROM.write(1,1);
  delay(5);
  bitWrite(_status,7,1);

  
}

if (command.substring(0,2) == "*T")
{
 bitWrite(_status,7,1);
 bitWrite(_status,6,1);
 command.trim();
 
int tl = command.length();
 
String time = command.substring(2,tl);
 
  myRTC.seconds = time.substring(4,6).toInt();
  myRTC.minutes = time.substring(2,4).toInt();
  myRTC.hours =   time.substring(0,2).toInt();
  myRTC.year = time.substring(10,14).toInt();
  myRTC.month = time.substring(8,10).toInt();
  myRTC.dayofmonth = time.substring(6,8).toInt();

 myRTC.setDS1302Time (myRTC.seconds, myRTC.minutes, myRTC.hours , 1, myRTC.dayofmonth, myRTC.month ,myRTC.year );
 
 //Serial.println(time);
}
if (command.substring(0,2) == "*B")
{
  bitWrite(_status,7,1);
  memset (RM, 0, sizeof(30));//reset del array
  for (int lc = 0; lc < 29 ; lc += 1)
 {
RM [lc] = 0;

}
  
  EEPROM.write(1,0);
  delay(5);

 for (int lc = 3; lc < len-2 ; lc += 1)
 {
RM [lc-3] = char(buf[lc]);// relay msg
}
  
  
  delay (10);
   
  }
  if (command.substring(0,2) == "*V")
  {
      int CW = EEPROM.read(9);
  if (CW == 0)
      {
        EEPROM.write(9,1);
  }
        else EEPROM.write(9,0);

        bitWrite(_status,7,1);

        }

        }
 
     }
    
    }
    rf22.spiWrite(0x71, 0x00); // unmodulated carrier
    }
}  
rf22.setModeIdle();

 }
 //****************************************************************** 

 

boolean matchInputSignal(byte s0, byte s1, byte s2, byte s3, byte s4)
{
  return ((inputSignal[0] == s0) && 
          (inputSignal[1] == s1) && 
          (inputSignal[2] == s2) && 
          (inputSignal[3] == s3) &&  
          (inputSignal[4] == s4));
}

// convert input signal to letter or ? if not found

char currentInputSignalToLetter()

{  
  if (matchInputSignal(DOT, DASH, NONE, NONE, NONE))  { return 'A'; }
  if (matchInputSignal(DASH, DOT, DOT, DOT, NONE))    { return 'B'; }
  if (matchInputSignal(DASH, DOT, DASH, DOT, NONE))   { return 'C'; }
  if (matchInputSignal(DASH, DOT, DOT, NONE, NONE))   { return 'D'; }
  if (matchInputSignal(DOT, NONE, NONE, NONE, NONE))  { return 'E'; }
  if (matchInputSignal(DOT, DOT, DASH, DOT, NONE))    { return 'F'; }
  if (matchInputSignal(DASH, DASH, DOT, NONE, NONE))  { return 'G'; }
  if (matchInputSignal(DOT, DOT, DOT, DOT, NONE))     { return 'H'; }
  if (matchInputSignal(DOT, DOT, NONE, NONE, NONE))   { return 'I'; }
  if (matchInputSignal(DOT, DASH, DASH, DASH, NONE))  { return 'I'; }
  if (matchInputSignal(DASH, DOT, DASH, NONE, NONE))  { return 'K'; }
  if (matchInputSignal(DOT, DASH, DOT, DOT, NONE))    { return 'L'; }
  if (matchInputSignal(DASH, DASH, NONE, NONE, NONE)) { return 'M'; }
  if (matchInputSignal(DASH, DOT, NONE, NONE, NONE))  { return 'N'; }
  if (matchInputSignal(DASH, DASH, DASH, NONE, NONE)) { return 'O'; }
  if (matchInputSignal(DOT, DASH, DASH, DOT, NONE))   { return 'P'; }
  if (matchInputSignal(DASH, DASH, DOT, DASH, NONE))  { return 'Q'; }
  if (matchInputSignal(DOT, DASH, DOT, NONE, NONE))   { return 'R'; }
  if (matchInputSignal(DOT, DOT, DOT, NONE, NONE))    { return 'S'; }
  if (matchInputSignal(DASH, NONE, NONE, NONE, NONE)) { return 'T'; }
  if (matchInputSignal(DOT, DOT, DASH, NONE, NONE))   { return 'U'; }
  if (matchInputSignal(DOT, DOT, DOT, DASH, NONE))    { return 'V'; }
  if (matchInputSignal(DOT, DASH, DASH, NONE, NONE))  { return 'W'; }
  if (matchInputSignal(DASH, DOT, DOT, DASH, NONE))   { return 'X'; }
  if (matchInputSignal(DASH, DOT, DASH, DASH, NONE))  { return 'Y'; }
  if (matchInputSignal(DASH, DASH, DOT, DOT, NONE))   { return 'Z'; }
  if (matchInputSignal(DOT, DASH, DASH, DASH, DASH))  { return '1'; }
  if (matchInputSignal(DOT, DOT, DASH, DASH, DASH))   { return '2'; }
  if (matchInputSignal(DOT, DOT, DOT, DASH, DASH))    { return '3'; }
  if (matchInputSignal(DOT, DOT, DOT, DOT, DASH))     { return '4'; }
  if (matchInputSignal(DOT, DOT, DOT, DOT, DOT))      { return '5'; }
  if (matchInputSignal(DASH, DOT, DOT, DOT, DOT))     { return '6'; }
  if (matchInputSignal(DASH, DASH, DOT, DOT, DOT))    { return '7'; }
  if (matchInputSignal(DASH, DASH, DASH, DOT, DOT))   { return '8'; }
  if (matchInputSignal(DASH, DASH, DASH, DASH, DOT))  { return '9'; }
  if (matchInputSignal(DASH, DASH, DASH, DASH, DASH)) { return '0'; }
  return '?';
}

// turn on the LED for the specified duration in milliseconds

// show signal (DOT or DASH) via LED 
boolean showSignal(byte dotDashNone)
{
  switch(dotDashNone) 
  {
    case DOT:
      
      return true;
    case DASH:
      
      return true;
    default:
      return false;
  }
}




 // Address is a page address, 6-bit (63). More and end will wrap around
// But data can be maximum of 28 bytes, because the Wire library has a buffer of 32 bytes


void readEEPROM(int deviceaddress, unsigned int eeaddress, unsigned char* data, unsigned int num_chars)
{   
  unsigned char i=0;   
  Wire.beginTransmission(deviceaddress);   
  Wire.write((int)(eeaddress >> 8)); // MSB   
  Wire.write((int)(eeaddress & 0xFF)); // LSB   
  Wire.endTransmission();     
  Wire.requestFrom(deviceaddress,num_chars);     
  while(Wire.available()) data[i++] = Wire.read();
}


void i2c_eeprom_write_page ( int deviceaddress, unsigned int eeaddresspage, char* data, byte length )
{

  int c_ = 0;
  
  Wire.beginTransmission(deviceaddress);

  
  Wire.write ((int)(eeaddresspage >> 8)); // Address High Byte
  Wire.write ((int)(eeaddresspage & 0xFF)); // Address Low Byte
  
  do{
    Wire.write((byte) data[c_]);
    
    c_ ++;
    
  }  while((c <= length));
  
  Wire.endTransmission();
  delay(5);                           // need some delay
}



//************************************************************************************************************
void writeEEPROM(int deviceaddress, unsigned int eeaddresspage, char* data)
{
  unsigned char write_size = 15;
  
 int i_ = 0;
 int counter_= 0;
  
     Wire.beginTransmission(deviceaddress);
     
       Wire.write((int)(eeaddresspage >> 8));// Address High Byte
       Wire.write((int)(eeaddresspage & 0xFF)); // Address Low Byte
              
     do{ 
        Wire.write( byte (data[i_]));
       // Wire.write((byte*) (data[i]));
        i_ = i_ + 1;
        
        counter_ ++;
        
     } while((data[i_]) && (counter_ <=15));
       
     Wire.endTransmission();
     
     //eeaddresspage+= write_size;   // Increment address for next write
     
     delay(6);  // needs 5ms for page write
}

void i2c_eeprom_write_page1( int deviceaddress, unsigned int eeaddresspage, byte* data, byte length ) 
{
Wire.beginTransmission(deviceaddress);

Wire.write((int)(eeaddresspage >> 8)); // MSB
Wire.write((int)(eeaddresspage & 0xFF)); // LSB
 
byte _c;

for ( _c = 0; _c < length; _c++)

Wire.write(data[ _c ]);

Wire.endTransmission();
}
