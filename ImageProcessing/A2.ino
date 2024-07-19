#include <Servo.h>

Servo myServo;
int servoPin = 9;  // El pin al que está conectado el servo

void setup() {
  Serial.begin(9600);  // Iniciar la comunicación serie
  myServo.attach(servoPin);  // Adjuntar el servo al pin
  myServo.write(0);  // Iniciar el servo en la posición cerrada (0 grados)
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');  // Leer la línea enviada desde Python
    int position = input.toInt();  // Convertir la cadena recibida en un número entero
    myServo.write(position);  // Mover el servo a la posición especificada
  }
}
