void setup() {
  // Set pin 15 as an output pin
  pinMode(12, OUTPUT);
  pinMode(8, OUTPUT);
}

void loop() {
  // Turn pin 15 HIGH (5V)
  digitalWrite(12, HIGH);
  digitalWrite(8, HIGH);
  delay(1000); // Wait 1 second

  // Turn pin 15 LOW (0V)
  digitalWrite(12, LOW);
  digitalWrite(8,LOW);
  delay(1000); // Wait 1 second
}