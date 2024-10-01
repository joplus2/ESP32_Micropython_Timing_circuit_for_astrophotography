# config file for inputs and outputs
from machine import Pin

#input definition
btnEnter = Pin(27, Pin.IN, Pin.PULL_DOWN)
btnDwnS  = Pin(26, Pin.IN, Pin.PULL_DOWN)
btnUpS   = Pin(25, Pin.IN, Pin.PULL_DOWN)
btnDwnDec= Pin(15, Pin.IN, Pin.PULL_DOWN)
btnUpDec = Pin(12, Pin.IN, Pin.PULL_DOWN)

#output definition
outCamShoot = Pin(23, Pin.OUT)
