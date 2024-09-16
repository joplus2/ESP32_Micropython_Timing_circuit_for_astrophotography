# This file is executed on every boot (including wake-boot from deepsleep)
import esp
#esp.osdebug(None)
import webrepl
webrepl.start()

#import
from machine import Pin, SPI

#rozsviceni LED pro BOOT
bootLed = Pin(2, Pin.OUT)
bootLed.on()

# reset displeje
"""
from st7735 import TFT, TFTRotations

tft = TFT(SPI(1), 16, 17, 18)
tft._reset()
tft.on(True)
tft.initr()
tft.invertcolor(True)
tft.rotation(TFTRotations[3])
tft.fill()
"""

from disp import st7789
from disp import vga_16x32
tft = st7789.ST7789(SPI(1), 240, 320, Pin(17, Pin.OUT),
                    Pin(16, Pin.OUT), Pin(18, Pin.OUT),
                    None, 1)
string = 'Inicializace'
tft.text(vga_16x32, string, 40, 100)

#input definition
global btnEnter
btnEnter = Pin(27, Pin.IN, Pin.PULL_DOWN)
global btnDwnS
btnDwnS  = Pin(26, Pin.IN, Pin.PULL_DOWN)
global btnUpS
btnUpS   = Pin(25, Pin.IN, Pin.PULL_DOWN)
global btnDwnDec
btnDwnDec= Pin(15, Pin.IN, Pin.PULL_DOWN)
global btnUpDec
btnUpDec = Pin(12, Pin.IN, Pin.PULL_DOWN)

# nastavení WiFi AP
import network
wlan = network.WLAN(network.AP_IF)	#vytvoření AP
wlan.config(ssid='Ahoj Karas!')		# nastavení SSID
wlan.config(max_clients=1)			# nastavení max počtu
wlan.active(True)					# zapnutí AP

# nastavení BT
import bluetooth
bt = bluetooth.BLE()
bt.config(bond=True)
bt.active(True)

#vypnuti boot LED
bootLed.off()
