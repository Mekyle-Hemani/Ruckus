const int stepPinF = 3; 
const int dirPinF = 4; 

const int stepPinR = 5;
const int dirPinR = 6;

const int stepPinU = 7; 
const int dirPinU = 8;

const int stepPinD = 9;
const int dirPinD = 10;

const int stepPinL = 11; 
const int dirPinL = 12;

const int stepPinB = 13;
const int dirPinB = 14;
 
void setup() {
  // Sets the two pins as Outputs
  pinMode(stepPinF,OUTPUT); 
  pinMode(dirPinF,OUTPUT);

  pinMode(stepPinR,OUTPUT); 
  pinMode(dirPinR,OUTPUT);

  pinMode(stepPinU,OUTPUT); 
  pinMode(dirPinU,OUTPUT);

  pinMode(stepPinD,OUTPUT); 
  pinMode(dirPinD,OUTPUT);

  pinMode(stepPinL,OUTPUT); 
  pinMode(dirPinL,OUTPUT);

  pinMode(stepPinB,OUTPUT); 
  pinMode(dirPinB,OUTPUT);
}
void loop() {
  digitalWrite(dirPinF,HIGH); // Enables the motor to move in a particular direction
  digitalWrite(dirPinR,HIGH);
  digitalWrite(dirPinU,HIGH);
  digitalWrite(dirPinD,HIGH);
  digitalWrite(dirPinL,HIGH);
  digitalWrite(dirPinB,HIGH);
  // Makes 200 pulses for making one full cycle rotation
  for(int x = 0; x < 200; x++) {
    digitalWrite(stepPinF,HIGH); 
    digitalWrite(stepPinR,HIGH);
    digitalWrite(stepPinU,HIGH); 
    digitalWrite(stepPinD,HIGH); 
    digitalWrite(stepPinL,HIGH); 
    digitalWrite(stepPinB,HIGH); 
    delayMicroseconds(500); 
    digitalWrite(stepPinF,LOW);
    digitalWrite(stepPinR,LOW);
    digitalWrite(stepPinU,LOW);
    digitalWrite(stepPinD,LOW);
    digitalWrite(stepPinL,LOW);
    digitalWrite(stepPinB,LOW);
    delayMicroseconds(500); 
  }
  delay(1000); // One second delay
  
  digitalWrite(dirPinF,LOW); //Changes the rotations direction
  digitalWrite(dirPinR,LOW);
  digitalWrite(dirPinU,LOW);
  digitalWrite(dirPinD,LOW);
  digitalWrite(dirPinL,LOW);
  digitalWrite(dirPinB,LOW);
  // Makes 400 pulses for making two full cycle rotation
  for(int x = 0; x < 400; x++) {
    digitalWrite(stepPinF,HIGH); 
    digitalWrite(stepPinR,HIGH);
    digitalWrite(stepPinU,HIGH); 
    digitalWrite(stepPinD,HIGH); 
    digitalWrite(stepPinL,HIGH); 
    digitalWrite(stepPinB,HIGH); 
    delayMicroseconds(500); 
    digitalWrite(stepPinF,LOW);
    digitalWrite(stepPinR,LOW);
    digitalWrite(stepPinU,LOW);
    digitalWrite(stepPinD,LOW);
    digitalWrite(stepPinL,LOW);
    digitalWrite(stepPinB,LOW);
    delayMicroseconds(500); 
  }
  delay(1000);
}