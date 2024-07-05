void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readString();
    if (data.indexOf("hi") >= 0) {
      digitalWrite(LED_BUILTIN, HIGH);
    }
    Serial.println("Received: " + data);
  }
}