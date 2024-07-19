#include <Servo.h>

Servo myServo;  // Crear un objeto servo

int servoPin = 9;  // Pin al que está conectado el servo
int angle = 0;  // Ángulo inicial del servo
int increment = 30;  // Incremento del ángulo en grados
int delayTime = 1000;  // Tiempo de retraso en milisegundos

void setup() {
  myServo.attach(servoPin);  // Adjuntar el servo al pin
  myServo.write(angle);  // Establecer el ángulo inicial del servo
}

void loop() {
  for (angle = 0; angle <= 180; angle += increment) {
    myServo.write(angle);  // Mover el servo al ángulo especificado
    delay(delayTime);  // Esperar un segundo
  }
  
  for (angle = 180; angle >= 0; angle -= increment) {
    myServo.write(angle);  // Mover el servo al ángulo especificado
    delay(delayTime);  // Esperar un segundo
  }
}
