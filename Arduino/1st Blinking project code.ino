void setup() {
  // Set pin 15 as an output pin
  pinMode(12, OUTPUT);
}

void loop() {
  // Turn pin 15 HIGH (5V)
  digitalWrite(12, HIGH);
  delay(100); // Wait 1 second

  // Turn pin 15 LOW (0V)
  digitalWrite(12, LOW);
  delay(100); // Wait 1 second
}
