
void SetupPACKET() {
  AX25Client ax25(&radio);
  // initialize SX1278
  // Serial.print(F("[SX1278] Initializing ... "));
  // carrier frequency:           434.0 MHz
  // bit rate:                    1.2 kbps (1200 baud 2-FSK AX.25)

  int state = radio.beginFSK(434.0, 1.2);

  // when using one of the non-LoRa modules for AX.25
  // (RF69, CC1101,, Si4432 etc.), use the basic begin() method
  // int state = radio.begin();

  if (state == RADIOLIB_ERR_NONE) {
    //   Serial.println(F("success!"));
  } else {
    Serial.print(F("failed, code "));
    Serial.println(state);
    while (true)
      ;
  }
  // initialize AX.25 client
  Serial.println(F("[AX.25] Initializing ... "));
  // source station callsign:     "N7LEM"
  // source station SSID:         0
  // preamble length:             8 bytes
  state = ax25.begin("LW2DTZ");
  if (state == RADIOLIB_ERR_NONE) {
    //  Serial.println(F("success!"));
  } else {
    Serial.print(F("failed, code "));
    Serial.println(state);
    while (true)
      ;
  }
}


void sendPACKET() {
  AX25Client ax25(&radio);

  SetupPACKET();

  // send AX.25 unnumbered information frame

  Serial.println(F("[AX.25] Sending UI frame ... "));

  // destination station callsign:     "NJ7P"
  // destination station SSID:         0
  //int state = ax25.transmit("Hello World!", "NJ7P");

  int state = ax25.transmit(superbuffer, "QST");

  if (state == RADIOLIB_ERR_NONE) {
    // the packet was successfully transmitted
    // Serial.println(F("success!"));
    // Serial.println(txt);

    //Serial.println(radio.getRSSI(true));

  } else {
    // some error occurred
    Serial.print(F("failed, code "));
    Serial.println(state);
  }
}
