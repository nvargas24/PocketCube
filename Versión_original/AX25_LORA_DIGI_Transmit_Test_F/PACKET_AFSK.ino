//AFSKClient audio(&radio, 4);
// create AX.25 client instance using the AFSK instance
//AX25Client ax25(&audio);

void AfskSetup() {
  AFSKClient audio(&radio, 4);

  // create AX.25 client instance using the AFSK instance

  AX25Client ax25(&audio);

  int state = radio.beginFSK();
  state = radio.setOutputPower(10);

  // when using one of the non-LoRa modules for AX.25
  // (RF69, CC1101,, Si4432 etc.), use the basic begin() method
  // int state = radio.begin();

  if (state == RADIOLIB_ERR_NONE) {
    Serial.println(F("success!"));
  } else {
    Serial.print(F("failed, code "));
    Serial.println(state);
    while (true)
      ;
  }

  // initialize AX.25 client
  Serial.print(F("[AX.25] Initializing ... "));
  // source station callsign:     "LW2DTZ"
  // source station SSID:         0
  // preamble length:             8 bytes
  state = ax25.begin("LW2DTZ");
  if (state == RADIOLIB_ERR_NONE) {
    Serial.println(F("success!"));
  } else {
    Serial.print(F("failed, code "));
    Serial.println(state);
    while (true)
      ;
  }

  // Sometimes, it may be required to adjust audio
  // frequencies to match the expected 1200/2200 Hz tones.
  // The following method will offset mark frequency by
  // 100 Hz up and space frequency by 100 Hz down

  Serial.print(F("[AX.25] Setting correction ... "));
  state = ax25.setCorrection(10, -10);
  if (state == RADIOLIB_ERR_NONE) {
    Serial.println(F("success!"));
  } else {
    Serial.print(F("failed, code "));
    Serial.println(state);
    while (true)
      ;
  }


  // send AX.25 unnumbered information frame

  Serial.print(F("[AX.25] Sending UI frame ... "));

  // destination station callsign:     "LW2DTZ"
  // destination station SSID:         0
  // state = ax25.transmit("Hello World!", "LW2DTZ");
  Serial.print(F("[AFSK] 400 Hz tone ... "));
  audio.tone(0);
  delay(250);
  audio.noTone();
  state = ax25.transmit(superbuffer, "QST");

  if (state == RADIOLIB_ERR_NONE) {
    // the packet was successfully transmitted
    Serial.println(F("success!"));

  } else {
    // some error occurred
    Serial.print(F("failed, code "));
    Serial.println(state);
  }
}


/*
void SendAfskLoop()
{

  afskSetup();
  
  AFSKClient audio(&radio, 4);
  AX25Client ax25(&audio);
  
  // send AX.25 unnumbered information frame
  
  Serial.print(F("[AX.25] Sending UI frame ... "));
  
  // destination station callsign:     "NJ7P"
  // destination station SSID:         0
  int state = ax25.transmit("Hello World!", "NJ7P");
  
  //int state = ax25.transmit(superbuffer, "QST");
  
  if (state == RADIOLIB_ERR_NONE)
  {
    // the packet was successfully transmitted
    Serial.println(F("success!"));

  } 
  else 
  {
    // some error occurred
    Serial.print(F("failed, code "));
    Serial.println(state);

  }

  
}
*/
