# config file for inputs and outputs
from machine import Pin

#input definition
btnEnter = Pin(28, Pin.IN, Pin.PULL_UP)
btnDwnS  = Pin(26, Pin.IN, Pin.PULL_UP)
btnUpS   = Pin(9,  Pin.IN, Pin.PULL_UP)
btnDwnDec= Pin(15, Pin.IN, Pin.PULL_UP)
btnUpDec = Pin(12, Pin.IN, Pin.PULL_UP)

#output definition
outCamShoot = Pin(6, Pin.OUT)
bootLed = Pin("LED", Pin.OUT)
