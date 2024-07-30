void sendmsg(char *str)
{
  while (*str)
    send(*str++) ;
 // Serial.println("");
}
