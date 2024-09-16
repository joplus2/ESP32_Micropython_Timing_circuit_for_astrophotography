from machine import Pin, SPI
from time import sleep
from disp import vga_16x32
from cam.CamSetup import SetupFun
from cam.CamShoot import ShootFun

global Setup
Setup = False 
global Shoot
Shoot = False
global Settings
Settings = [0, 0, 0, False]

global TimeShoot        # délka závěrky fotoaparátu
TimeShoot = 0
global TimeBtween       # čas mezi fotkami
TimeBtween = 0
global ShootCount       # počet fotek
ShootCount = 0

# zobrazení hlášky
string = 'Zacnete ENTERem'
tft.text(vga_16x32, string, 40, 100)

# funkce spouštějící nastavení
def StartSetup(self):
    global Setup
    global Shoot
    global Settings
    global TimeShoot
    global TimeBtween
    global ShootCount
    global tft
    string = 'Spousteni nastaveni            '
    tft.text(vga_16x32, string, 10, 100)
    sleep(1)
    Setup = True
    if ( Setup == True ):
        Settings = SetupFun(Setup, TimeShoot, TimeBtween, ShootCount, tft)
        TimeShoot = Settings[0]
        TimeBtween = Settings[1]
        ShootCount = Settings[2]
        Shoot = Settings[3]
        Setup = False
    if ( Shoot == True ):
        string = 'Probiha foceni...          '
        tft.text(vga_16x32, string, 10, 100)
        ShootFun(Shoot, TimeShoot, TimeBtween, ShootCount)
        Shoot = False
    string = 'Dokonceno              '
    tft.text(vga_16x32, string, 10, 100)
    sleep(2)
    string = 'Zacnete ENTERem        '
    tft.text(vga_16x32, string, 10, 100)
    return

#interrupt na enter pro start nastavení
if ( Setup == False  ) and ( Shoot == False ):
    btnEnter.irq( trigger = Pin.IRQ_RISING, handler = StartSetup)

"""
if ( Setup == True ):
    Settings = CamSetup.SetupFun(Setup, TimeShoot, TimeBtween, ShootCount)
    TimeShoot = Settings[0]
    TimeBtween = Settings[1]
    ShootCount = Settings[2]
    Shoot = Settings[3]
    Setup = False

if ( Shoot == True):
    CamShoot.ShootFun(Shoot, TimeShoot, TimeBtween, ShootCount)
    Shoot = False
"""
