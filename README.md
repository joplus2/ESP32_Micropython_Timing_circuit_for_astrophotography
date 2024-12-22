# Timing circuit for astrophotography

## Introduction
This repository is dedicated to my bachelors thesis - timing circuit for astrophotography. Here is my whole progress and all the files.

## Recomended outline

### BP(K)C-SEP: 
- Prostudujte metody focení trajektorie hvězd tzv. „star trails“
- Navrhněte vhodný číslicově řízený obvod pro časování spouštění závěrky fotoaparátu
- Předpokládejte řízení fotoaparátu přes rozhraní dálkového (kabelového) spouštění expozice, ale zvažte i možnost řízení pomocí tzv. „camera tethering“ založeného na USB komunikaci
- Zvolte vhodné a zvládnutelné řešení, navrhněte HW a v případě využití mikrokontroleru i SW řešení
- Ověřte základní činnost časovače
### BP(K)C-BAP:
- Realizujte kompletní časovací obvod s rozhraním pro komunikaci s fotoaparátem
- Mechanické řešeni a celý časovač realizujte a ověřte jeho činnost
- Zvolte napájení časovače z baterií nebo akumulátoru s možností nabíjení (preferováno)
- Zpracujte kompletní technickou dokumentaci k HW i SW části práce

## Microcontroler selection

## Microcontroller pinout
### Display interface for ESP32:
SPI(1):
- SCK pin: 14
- MOSI pin: 13

Library:
- Reset pin: 17
- DC pin: 16
- CS pin: 18

### Display interface for RPi Pico 2:
SPI(1):
- SCK pin: 10
- MOSI pin: 11

Library:
- Reset pin: 17
- DC pin: 16
- CS pin: 18

### Input definitions:
- Enter button: pin 27
- Seconds down button: pin 26
- Seconds up button: pin 25
- Decimals down button: pin 15
- Decimals up button: pin 12

### Output definitoions:
- Camera shoot: pin 23
- reserve for camera focus?


## References

[Display ST7789 driver](https://github.com/russhughes/st7789_mpy)
