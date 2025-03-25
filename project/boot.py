#import
from machine import Pin, SPI
from config.io import *
from time import sleep
from config.functions import settingsConv
# display libraries
from disp import st7789
from disp import vga_16x32


# turning on BOOT status LED
bootLed = Pin(2, Pin.OUT)
bootLed.on()

# read current settings
f = open("/config/settings.txt", "r")
sysSettings = settingsConv(f.read())
f.close()

# set-up and initialize display
tft = st7789.ST7789(SPI(1), 240, 320, Pin(17, Pin.OUT),
                    Pin(16, Pin.OUT), Pin(18, Pin.OUT),
                    None, 1)
string = 'Inicializace'
tft.text(vga_16x32, string, 40, 100)

#vypnuti boot LED
bootLed.off()
