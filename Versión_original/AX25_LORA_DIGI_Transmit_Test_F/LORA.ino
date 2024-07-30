
// flag to indicate that a packet was received
//volatile bool receivedFlag = false;

// disable interrupt when it's not needed
//volatile bool enableInterrupt = true;

void SetupLoRa() {
  int state = radio.begin();

  state = radio.setFrequency(LORA_FREQUENCY);
  state = radio.setRxBandwidth(LORA_BANDWIDTH);
  state = radio.setSpreadingFactor(LORA_SPREADFACTOR);
  state = radio.setCodingRate(LORA_CODERATE);
  state = radio.setSyncWord(LORA_SYNCWORD);
  state = radio.setPreambleLength(LORA_PREAMBLELENGTH);
  state = radio.setOutputPower(LORA_POWER);
  state = radio.setGain(LORA_GAIN);

  if (state == RADIOLIB_ERR_NONE) {
    //  Serial.println(F("success!"));
  } else {
    Serial.print(F("failed, code "));
    Serial.println(state);
    while (true)
      ;
  }
}

void sendLoRa() {

  SetupLoRa();

  // Send the string
  Serial.println("LoRa sending..");
  int state = radio.transmit(superbuffer);
  delay(10);
}

void DIGI() {


  // you can receive data as an Arduino String
  // NOTE: receive() is a blocking method!
  //       See example ReceiveInterrupt for details
  //       on non-blocking reception method.
  String str;
  int state = radio.receive(str);

  // you can also receive data as byte array
  /*
    byte byteArr[8];
    int state = radio.receive(byteArr, 8);
  */

  if (state == RADIOLIB_ERR_NONE) {
    // packet was successfully received
    Serial.println(F("success!"));

    // print the data of the packet
    Serial.print(F("[SX1278] Data:\t\t\t"));


    // print the RSSI (Received Signal Strength Indicator)
    // of the last received packet
    Serial.print(F("[SX1278] RSSI:\t\t\t"));
    Serial.print(radio.getRSSI());
    Serial.println(F(" dBm"));

    // print the SNR (Signal-to-Noise Ratio)
    // of the last received packet
    Serial.print(F("[SX1278] SNR:\t\t\t"));
    Serial.print(radio.getSNR());
    Serial.println(F(" dB"));

    // print frequency error
    // of the last received packet
    Serial.print(F("[SX1278] Frequency error:\t"));
    Serial.print(radio.getFrequencyError());
    Serial.println(F(" Hz"));

    int state = radio.transmit("$$" + str);
    Serial.println("$$" + str);

  }
  /*
  else if (state == RADIOLIB_ERR_RX_TIMEOUT)
  {
    // timeout occurred while waiting for a packet
   // Serial.println(F("timeout!"));

  }
  */
  else if (state == RADIOLIB_ERR_CRC_MISMATCH) {
    // packet was received, but is malformed
    Serial.println(F("CRC error!"));

  } else {
    // some other error occurred
    Serial.print(F("failed, code "));
    Serial.println(state);
  }
}

/*

void setFlag(void)
{
  // check if the interrupt is enabled
  if (!enableInterrupt)
  {
    return;
  }

  // we got a packet, set the flag
  receivedFlag = true;
}


void SetRx() 
{
  SetupLoRa();

  // set the function that will be called
  // when new packet is received
  radio.setDio0Action(setFlag);

  // start listening for LoRa packets
  Serial.print(F("[SX1278] Starting to listen ... "));
  state = radio.startReceive();

  /*
  if (state == RADIOLIB_ERR_NONE)
  {
    Serial.println(F("success!"));
  }
  else
  {
    Serial.print(F("failed, code "));
    Serial.println(state);
    while (true);
  }
  
}

void Rxloop()
{
  // check if the flag is set
  
  if(receivedFlag)
  {
   
    // disable the interrupt service routine while
    // processing the data
    enableInterrupt = false;

    // reset flag
    receivedFlag = false;

    // you can read received data as an Arduino String
    String str;
    int state = radio.readData(str);

    // you can also read received data as byte array
    /*
      byte byteArr[8];
      int state = radio.readData(byteArr, 8);
    

    if (state == RADIOLIB_ERR_NONE) 
    {
      // packet was successfully received
      Serial.println(F("[SX1278] Received packet!"));

      // print data of the packet
      Serial.print(F("[SX1278] Data:\t\t"));
      Serial.println(str);

      // print RSSI (Received Signal Strength Indicator)
      Serial.print(F("[SX1278] RSSI:\t\t"));
      Serial.print(radio.getRSSI());
      Serial.println(F(" dBm"));

      // print SNR (Signal-to-Noise Ratio)
      Serial.print(F("[SX1278] SNR:\t\t"));
      Serial.print(radio.getSNR());
      Serial.println(F(" dB"));

      // print frequency error
      Serial.print(F("[SX1278] Frequency error:\t"));
      Serial.print(radio.getFrequencyError());
      Serial.println(F(" Hz"));

    }
    else if (state == RADIOLIB_ERR_CRC_MISMATCH) {
      // packet was received, but is malformed
      Serial.println(F("[SX1278] CRC error!"));

    }
    else 
    {
      // some other error occurred
      Serial.print(F("[SX1278] Failed, code "));
      Serial.println(state);

    }

    // put module back to listen mode
    radio.startReceive();

    // we're ready to receive more packets,
    // enable interrupt service routine
    enableInterrupt = true;
}
}
*/
