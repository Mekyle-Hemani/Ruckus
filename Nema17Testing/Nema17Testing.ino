const int stepPinF = 3; 
const int dirPinF = 4; 

const int stepPinR = 5;
const int dirPinR = 6;
 
void setup() {
  // Sets the two pins as Outputs
  pinMode(stepPinF,OUTPUT); 
  pinMode(dirPinF,OUTPUT);

  pinMode(stepPinR,OUTPUT); 
  pinMode(dirPinR,OUTPUT);
}
void loop() {
  digitalWrite(dirPinF,HIGH); // Enables the motor to move in a particular direction
  digitalWrite(dirPinR,HIGH);
  // Makes 200 pulses for making one full cycle rotation
  for(int x = 0; x < 200; x++) {
    digitalWrite(stepPinF,HIGH); 
    digitalWrite(stepPinR,HIGH); 
    delayMicroseconds(500); 
    digitalWrite(stepPinF,LOW);
    digitalWrite(stepPinR,LOW);
    delayMicroseconds(500); 
  }
  delay(1000); // One second delay
  
  digitalWrite(dirPinF,LOW); //Changes the rotations direction
  digitalWrite(dirPinR,LOW);
  // Makes 400 pulses for making two full cycle rotation
  for(int x = 0; x < 400; x++) {
    digitalWrite(stepPinF,HIGH);
    digitalWrite(stepPinR,HIGH);
    delayMicroseconds(500);
    digitalWrite(dirPinF,LOW);
    digitalWrite(dirPinR,LOW);
    delayMicroseconds(500);
  }
  delay(1000);
}