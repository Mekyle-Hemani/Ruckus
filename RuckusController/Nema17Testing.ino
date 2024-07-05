const int dirPin = 4;
const int stepPin = 3;
const int stepsPerRevolution = 200;

void setup()
{
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
}
void loop()
{
  digitalWrite(dirPin, HIGH);

  for(int x = 0; x < stepsPerRevolution; x++)
  {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(500);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(500);
  }
  delay(500);

  spin(200, 1, 400); 
}

void spin(int count, int dir, int del){
  digitalWrite(dirPin, dir);
  for (int i=0; i<count; i++){
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(del);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(del);
  }
}
