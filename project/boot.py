# This file is executed on every boot (including wake-boot from deepsleep)
import esp
#esp.osdebug(None)
import webrepl
webrepl.start()

#import
from machine import Pin, SPI
from config.io import *

#rozsviceni LED pro BOOT
bootLed.on()

from disp import st7789
from disp import vga_16x32
tft = st7789.ST7789(SPI(1), 240, 320, Pin(17, Pin.OUT),
                    Pin(16, Pin.OUT), Pin(18, Pin.OUT),
                    None, 1)
string = 'Inicializace'
tft.text(vga_16x32, string, 40, 100)

#vypnuti boot LED
bootLed.off()
