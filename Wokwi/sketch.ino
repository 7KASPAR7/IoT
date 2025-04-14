#include <Arduino.h>

// Определяем пины для RGB
const int redPin = 15;
const int greenPin = 14;
const int bluePin = 13;

// Функция для установки цвета
void setColor(int r, int g, int b) {
    digitalWrite(redPin, r);
    digitalWrite(greenPin, g);
    digitalWrite(bluePin, b);
}

void setup() {
    // Настройка пинов как выходы
    pinMode(redPin, OUTPUT);
    pinMode(greenPin, OUTPUT);
    pinMode(bluePin, OUTPUT);
}

void loop() {
    setColor(HIGH, LOW, LOW);   // Красный
    delay(1000);
    setColor(LOW, HIGH, LOW);   // Зеленый
    delay(1000);
    setColor(LOW, LOW, HIGH);   // Синий
    delay(1000);
    setColor(HIGH, HIGH, LOW);   // Желтый
    delay(1000);
    setColor(LOW, HIGH, HIGH);   // Циан
    delay(1000);
    setColor(HIGH, LOW, HIGH);   // Магента
    delay(1000);
    setColor(LOW, LOW, LOW);     // Выключить
    delay(1000);
}