""" functions related to camera """
from network import WLAN
import network
from disp import vga_16x32
from time import sleep
from config.io import *
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
    
def wiredShutter(TimeShoot):
    outCamShoot.on()
    sleep(TimeShoot)
    outCamShoot.off()
    
def ptpipShutter(ptpip):
    # command to start shooting
    ptpip_cmd = PtpIpCmdRequest(cmd=0x9207, param1=0xffffffff, param2=0x0000)
    ptpip_packet = ptpip.send_ptpip_cmd(ptpip_cmd)

    sleep(TimeShoot)

    # command to stop shooting
    ptpip_cmd = PtpIpCmdRequest(cmd=0x920C, param1=0xffffffff, param2=0x0000)
    ptpip_packet = ptpip.send_ptpip_cmd(ptpip_cmd)
    
