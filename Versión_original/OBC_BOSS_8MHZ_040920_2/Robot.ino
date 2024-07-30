 void Robot()
 {
  rf22.setModeRx();

 long currentTimestamp  = millis(); // get the current timestamp
  
  long duration = currentTimestamp - lastTimestamp; // get elapsed time
  
  w = ((int)rf22.rssiRead()*51 - 12400)/100; 
  
  //Serial.println(w);// print rssi value
  
  //if (digitalRead(BUTTON) == LOW) 
  if (w > -60)// read rfm22 rssi value
  { // if the button is pressed
    
    if (!buttonWasPressed)
    
    { //  if the button was previously not pressed
      buttonWasPressed = true; // remember the button press
      
      lastTimestamp = currentTimestamp;// record the time of the button press
      
      if (duration > LETTER_GAP)
      {
       // Serial.print(' ');
        j = j + 1;
        X = X + " ";
      }
    } // end of if (button was not pressed)
  }
   
  else
  
  { // the button is not pressed
    if (buttonWasPressed) 
    {  // the button was just released
      if (duration < DOT_DURATION)
      { // if the button was pressed for up to DOT cutoff
        inputSignal[inputSignalIndex] = DOT; // remember the current signal as a DOT
      } else { // if the button was pressed for longer than DOT cutoff
        inputSignal[inputSignalIndex] = DASH; // remember the current signal as a DASH
      }
      inputSignalIndex++; // advance the index to the input signal buffer
                  
      buttonWasPressed = false; // consume previous button press
      
      lastTimestamp = currentTimestamp; // record the time the button was released
      
    }
    else 
    { // the button was not just released
      
      if (inputSignalIndex > 0)
      
      { // if there is data in the input signal buffer
        
        if (duration > SIGNAL_GAP || inputSignalIndex >= 5)
        
        { // if we have a complete letter
        
          //Serial.print(currentInputSignalToLetter()); // parse the letter and send it via serial
          
          F = String (currentInputSignalToLetter());
          
          X = X + F;
          //Serial.print(F);
         
          j =j+1;

          //if (j==18)
          
          //if (j == (19+_K))
          if (j == _P)
          {flg1 = true;}
          
          resetInputSignal(); // reset the input signal buffer
        }
 
      }
      
    } // end of else (button was not previously pressed)
    
  } // end of else (button is not pressed)
  
 }
