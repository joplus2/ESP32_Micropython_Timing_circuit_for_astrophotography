from machine import Pin, SPI,disable_irq, enable_irq
from time import sleep
from sys import exit
# font libraries
from disp import vga_16x32
from disp import vga_8x16
# camera related libraries
from cam.CamSetup import SetupFun
from cam.CamShoot import ShootFun
from cam.functions import NikonConn
# configuration libraries
from config.io import *
from config.settings import mcuSettings
# PTP/IP libraries
from nikon.ptpip import PtpIpConnection
from nikon.ptpip import PtpIpCmdRequest
from nikon.threading import Thread

""" for WLAN settings """
string = 'Podrzenim ENTER zobrazit nastaveni'
tft.text(vga_8x16, string, 30, 220)

sleep(0.5)

# settings startup logic
count = 0
btnHold = 0

while count < 5:
    if btnEnter.value():
        btnHold = btnHold + 1
    sleep(0.5)
    count = count + 1
    
# remove settings text by making black rectangle
tft.fill_rect(0, 220, 320, 16, st7789.BLACK)
    
if btnHold >= 4:
    string = 'Nastaveni             '
    tft.text(vga_16x32, string, 40, 100)
    sleep(1)
    mcuSettings(tft, sysSettings)

""" calling WiFi connect and start services """
if ( sysSettings[0] == True ):
    string = "Spousteni WiFi           "
    tft.text(vga_16x32, string, 10, 100)
    NikonConn(tft, sysSettings)
    string = "Spousteni sluzeb         "
    tft.text(vga_16x32, string, 10, 100)
    try:
        ptpip = PtpIpConnection()
        ptpip.open()
        thread = Thread(target=ptpip.communication_thread)
        thread.daemon = True
        thread.start()
        sleep(1)
    except:
        string = "Nastala chyba         "
        tft.text(vga_16x32, string, 10, 100)
        exit()
    else:
        string = "Sluzby spusteny       "
        tft.text(vga_16x32, string, 10, 100)

""" asigning default values """
# bool pro vyvolání nastavení
Setup = False
# bool pro započetí focení
Shoot = False
# vystupni tupple z funkce
Settings = [0, 0, 0, False]

# délka závěrky fotoaparátu
TimeShoot = 0
# čas mezi fotkami
TimeBtween = 0
# počet fotek
ShootCount = 0
# bool pro vypsani textu
beginTxt = False

try:
    while (True):
        # zobrazení hlášky
        string = 'Zacnete ENTERem  '
        if (beginTxt == False):
            tft.text(vga_16x32, string, 10, 100)
            beginTxt = True
        
        # spusteni nastaveni pomoci ENTER
        if (btnEnter.value() == True):
            sleep(0.5)
            string = 'Spousteni nastaveni            '
            tft.text(vga_16x32, string, 10, 100)
            beginTxt = False
            sleep(1)
            Setup = True
        
        # spusteni nastaveni + prirazeni z tupple
        if ( Setup == True ):
            Settings = SetupFun(Setup, TimeShoot, TimeBtween, ShootCount, tft)
            TimeShoot = Settings[0]
            TimeBtween = Settings[1]
            ShootCount = Settings[2]
            Shoot = Settings[3]
            Setup = False
            
        # spusteni foceni
        if ( Shoot == True ):
            string = 'Probiha foceni...          '
            tft.text(vga_16x32, string, 10, 100)
            ShootFun(Shoot, TimeShoot, TimeBtween, ShootCount, tft, ptpip)
            Shoot = False
            string = 'Dokonceno              '
            tft.text(vga_16x32, string, 10, 100)
            sleep(2)
        
except KeyboardInterrupt:
    # This part runs when Ctrl+C is pressed
    print("Program stopped. Exiting...")
        









