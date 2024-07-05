void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);
  digitalWrite(13, LOW);
}

void loop() {
  if (Serial.available() > 0) {
     String data = Serial.readString();
    if (data == "hi"){
      digitalWrite(13, HIGH);
    }
  }
}