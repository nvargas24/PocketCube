#include <TimerOne.h>
#include <LiquidCrystal_I2C.h>
#include <Wire.h>

LiquidCrystal_I2C lcd(0x27,16,2);

int mostrar = 0;

const byte det1 = 2;

long int pulsos1=0;

long int decCPS1[10];
int x = 0;

float cps1=0;
float cpsMax=0;

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  attachInterrupt(digitalPinToInterrupt(det1), det1Pulse, RISING);

  Timer1.initialize(1000000);
  Timer1.attachInterrupt(ISR_CPS);

  lcd.begin();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("D1:");
  lcd.setCursor(8, 1);
  lcd.print("MAX:");
}

void loop() {
  if (mostrar==1){
    cps1=float(decCPS1[0]+decCPS1[1]+decCPS1[2]+decCPS1[3]+decCPS1[4])/5;
    
    Serial.println(cps1);

    if (cps1<9999)
      {
      lcd.setCursor(3, 0);
      lcd.print("     ");
      lcd.setCursor(3, 0);
      lcd.print(cps1,0);
      }
    else
      {
      lcd.setCursor(3, 0);
      lcd.print("ovf  ");
      }

    lcd.setCursor(12, 1);
    lcd.print("    ");
    lcd.setCursor(12, 1);
    lcd.print(cpsMax,0);

    mostrar=0;
  }  
}

void ISR_CPS(){
  decCPS1[x] = pulsos1;
  pulsos1=0;
  mostrar=1;

  x++;
  if (x==5) {
    x=0;
  }
}

void det1Pulse() {
  pulsos1++;
}
