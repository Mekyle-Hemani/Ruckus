#include <Arduino.h>

void setup() {
  Serial.begin(9600);
  while (!Serial){}
}

void loop() {
  Serial.println("hi");
  if (Serial.available() > 0) {
    String receivedData = Serial.readStringUntil('\n');
    Serial.print("Received: ");
    Serial.println(receivedData);
  }
}