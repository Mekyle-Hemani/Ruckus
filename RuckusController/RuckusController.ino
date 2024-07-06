const int ledPin = 12;
void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void grabSolve(String moves){
  digitalWrite(ledPin, HIGH);
  delay(1000);
  digitalWrite(ledPin, LOW);
  String movesTotal[moves.length()];
  int j = 0; // Index for movesTotal
  for (int i = 0; i < moves.length(); i++) {
    if (i < moves.length() - 1 && moves.charAt(i + 1) == 'p') {
      i++;
      i++;
      //Needs to turn it into a prime movement
    }
    movesTotal[j] = String(moves.charAt(i));
    j++;
  }
  for (int i = 0; i < moves.length(); i++) {
    if (movesTotal[i] != ""){
      Serial.println(movesTotal[i]);
    }
  }
  return;
}

void loop() {
  if (Serial.available()) {
    String message = Serial.readStringUntil('\n');
    grabSolve(message);
  } else {
      digitalWrite(ledPin, LOW);
  }
}