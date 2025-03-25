""" functions related to camera """
from network import WLAN
import network
from disp import vga_16x32
from time import sleep
global wlan

def NikonConn(tft, settings):
    global wlan
    wlan = network.WLAN(network.WLAN.IF_STA)
    wlan.active(True)
    wlan.connect(settings[1], settings[2])
    while not wlan.isconnected():
        string = "Pripojovani k WiFi...     "
        tft.text(vga_16x32, string, 10, 100)
    string = "Pripojeno k WiFi.       "
    tft.text(vga_16x32, string, 10, 100)
    sleep(1)
