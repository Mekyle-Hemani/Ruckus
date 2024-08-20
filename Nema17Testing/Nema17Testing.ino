const int stepPinF = 14; 
const int dirPinF = 12; 
 
void setup() {
  // Sets the two pins as Outputs
  pinMode(stepPinF,OUTPUT); 
  pinMode(dirPinF,OUTPUT);
}
void loop() {
  digitalWrite(dirPinF,HIGH); // Enables the motor to move in a particular direction
  // Makes 200 pulses for making one full cycle rotation
  for(int x = 0; x < 200; x++) {
    digitalWrite(stepPinF,HIGH); 
    delayMicroseconds(500); 
    digitalWrite(stepPinF,LOW);
    delayMicroseconds(500); 
  }
  delay(1000); // One second delay
  
  digitalWrite(dirPinF,LOW); //Changes the rotations direction
  // Makes 400 pulses for making two full cycle rotation
  for(int x = 0; x < 400; x++) {
    digitalWrite(stepPinF,HIGH); 
    delayMicroseconds(500); 
    digitalWrite(stepPinF,LOW);
    delayMicroseconds(500); 
  }
  delay(1000);
}