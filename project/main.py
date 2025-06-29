from machine import Pin, SPI
import network
from time import sleep
from sys import exit
# font libraries + disp lib
from disp import vga_16x32
from disp import vga_8x16
from disp.functions import showEnterBtn, vanishEnterBtn
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
    if not btnEnter.value():
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
ptpip = PtpIpConnection()
wlan = network.WLAN(network.WLAN.IF_STA)
wlan.active(False)
if ( sysSettings[0] == True ):
    string = "Spousteni WiFi           "
    tft.text(vga_16x32, string, 10, 100)
    wlan = NikonConn(tft, sysSettings)
    string = "Spousteni sluzeb         "
    tft.text(vga_16x32, string, 10, 100)
    try:
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
# show enter button
showEnterBtn(tft)

try:
    while (True):
        # zobrazení hlášky
        string = 'Zacnete ENTERem  '
        if (beginTxt == False):
            tft.text(vga_16x32, string, 10, 100)
            beginTxt = True
        
        # spusteni nastaveni pomoci ENTER
        if (btnEnter.value() == False):
            sleep(0.5)
            string = 'Spousteni nastaveni...         '
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
            vanishEnterBtn(tft)
            string = 'Probiha foceni...          '
            tft.text(vga_16x32, string, 10, 100)
            ShootFun(Shoot, TimeShoot, TimeBtween, ShootCount, tft, ptpip, sysSettings[0])
            Shoot = False
            string = 'Dokonceno              '
            tft.text(vga_16x32, string, 10, 100)
            sleep(2)
            showEnterBtn(tft)
        
        # if PTP/IP error occured
        from nikon.ptpip import ErrorFlag, CmdSuccess
        if ( ErrorFlag == True ):
            raise ValueError('PTPIP_err')
            
        # to close PTP/IP connection
        if ( btnUpS.value() == False  ) and \
           ( btnDwnS.value() == False ) and \
           ( sysSettings[0] == True   ):
            # command to close PTP/IP session
            ptpip_cmd = PtpIpCmdRequest(cmd=0x1003, param1=0xffffffff, param2=0x0000)
            ptpip_packet = ptpip.send_ptpip_cmd(ptpip_cmd)
            if ( CmdSuccess == True ):
                tft.text(vga_16x32, 'PTP/IP session zavrena', 10, 100)
            
            
except KeyboardInterrupt:
    # This part runs when Ctrl+C is pressed
    print("Program stopped. Exiting...")
    
except ValueError as e:
    if ( e == 'PTPIP_err' ):
        string = 'Nastala chyba PTPIP   '
    else:
        string = "Nastala chyba         "
    tft.text(vga_16x32, string, 10, 100)
    string = 'Provedte restart   '
    tft.text(vga_16x32, string, 10, 140)
    exit()
