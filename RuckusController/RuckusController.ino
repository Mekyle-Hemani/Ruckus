void setup() {
  Serial.begin(9600);  // Start serial communication at 9600 baud
  pinMode(LED_BUILTIN, OUTPUT);
  while (!Serial) {
    ; // Wait for the serial port to connect.
  }
}

void loop() {
  if (Serial.available() > 0) {
    // Read incoming data
    String incomingData = Serial.readStringUntil('\n');

    // Check if "hi" is in the incoming data
    if (incomingData.indexOf("a") != -1) {
      digitalWrite(LED_BUILTIN, HIGH);
    }
  }
}