const int ledPin = 12;  // LED connected to digital pin 12

void setup() {
  Serial.begin(9600);  // Start serial communication at 9600 baud
  pinMode(ledPin, OUTPUT);  // Set LED pin as output
}

void loop() {
  if (Serial.available()) {
    String message = Serial.readStringUntil('\n');  // Read the incoming message

    if (message.indexOf("moveset") >= 0) {
      digitalWrite(ledPin, HIGH);  // Turn on the LED
    } else {
      digitalWrite(ledPin, LOW);  // Turn off the LED
    }
  }
}
