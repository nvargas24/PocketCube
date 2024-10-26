#include <TinyWireS.h>
void setup() {
  TinyWireS.begin(8);
}
void loop() {
  TinyWireS.send('1');
  delay(100);
}