void logger_out()
{
rf22.setModemRegisters(&FSK_500bd);

 _EEx =  loggcount ;
 
int lz = ((( _EEx )/16));
  
     for(int _k = 0; _k <= lz ; _k ++)
     {
      int addEE = _k * 16;
 
  readEEPROM(disk1,addEE, rdata, 15);
       
    sprintf (txbuffer,"$$%02d%02d%02d%02d%02d%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X*\n", rdata[0], rdata[1], rdata[2], rdata[3] ,rdata[4],rdata[5], rdata[6],rdata[7], rdata[8], rdata[9], rdata[10] ,rdata[11],rdata[12], rdata[13],rdata[14]);
    delay(5);
  
    //Serial.print(txbuffer);
     delay(5);
   
process_data (txbuffer);
   
   delay(500);

}
EEPROM.write(3,0);

delay (5);
}
