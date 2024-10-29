int verification = 0;
String incoming;

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  while (!Serial) {
  }
}

void loop() {
  if (verification == 0){
    if (Serial.available() > 0) {
      String incomingData = Serial.readStringUntil('\n');
      if (incomingData.indexOf("a") != -1) {
        incoming = incomingData;
        digitalWrite(LED_BUILTIN, HIGH);
        verification = 1;
      }
    }
  } else if (verification == 1){
    //Split incoming string
  }
}