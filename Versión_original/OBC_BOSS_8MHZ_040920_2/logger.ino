void logger_in()
{
  //  Serial.print("log= ");
    
  //  Serial.println( _EEx);

    wdata[0]= (uint8_t)  (myRTC.hours);
 
    wdata[1]= (uint8_t)  (myRTC.minutes);

    wdata[2]= (uint8_t) (myRTC.seconds);
 
    wdata[3]= (uint8_t) (myRTC.dayofmonth);

    wdata[4]= (uint8_t) (myRTC.month);

    wdata[5]= CBat;//CORRIENTE BATERIA
    
    wdata[6]= CBor;//CORRIENTE PLACA
    
    rf22.setModeRx();
    
    wdata[7]= (uint8_t) (rf22.temperatureRead( RF22_TSRANGE_M64_64C)& 0xFF) ;//TEMPERATURA RF AMP
    
    wdata[8]= _RSC;
            
    wdata[9]=  (uint8_t) (rf22.rssiRead() & 0xFF);//LECTURA RSSI

    rf22.setModeIdle();
     
    wdata[10]= (uint8_t)(battVolts&0xFF);//TENSION DE BATERIA

    wdata[11]= (uint8_t)(battVolts>>8);//TENSION DE BATERIA
    
    wdata[12]= (uint8_t)(t_cpu&0xFF);

    wdata[13]= (uint8_t)(t_cpu>>8);

    wdata[14]= (uint8_t)(MCUSRX>>8);
    
    i2c_eeprom_write_page1 (disk1, _EEx, (byte*)wdata, 15);
    
   
    LowPower.powerDown(SLEEP_8S, ADC_OFF, BOD_OFF);
    LowPower.powerDown(SLEEP_2S, ADC_OFF, BOD_OFF);
    
     _EEx = _EEx + 16;
        
      void heartbeat();

    if (  _EEx > loggcount )//112,1008   I----0----I----16----I---32---I---48----I / I---64----I----80----I---96---I--112----I
    {                           
      
     EEPROM.write (2 , 0);//SI SUPERA LA CANTIDAD DE VECES RESETEA LA DIRECCION EEPROM A 0
     delay(5);
     EEPROM.write(20,1);//LOGGER LLENO
     bitWrite(_status,4,1);
   //  Serial.println(F("seteo en cero"));
       
    }

}
