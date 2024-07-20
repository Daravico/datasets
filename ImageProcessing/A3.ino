#include <Servo.h>

const int potPin = A0;       // Pin del potenciómetro
const int servoPin = 9;      // Pin del servo

Servo myServo;

void setup() {
  Serial.begin(9600);
  myServo.attach(servoPin);
}

void loop() {
  // Leer el valor del potenciómetro (0-1023)
  int potValue = analogRead(potPin);

  // Enviar el valor del potenciómetro al PC
  Serial.println(potValue);

  // Leer el comando para el servo
  if (Serial.available() > 0) {
    int servoPosition = Serial.parseInt();
    // Mover el servo a la posición indicada
    if (servoPosition >= 0 && servoPosition <= 180) {
      myServo.write(servoPosition);
    }
  }

  delay(50); // Espera para evitar sobrecargar la comunicación serial
}
