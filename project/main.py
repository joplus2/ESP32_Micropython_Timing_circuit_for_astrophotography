from machine import Pin, SPI,disable_irq, enable_irq
from time import sleep
from disp import vga_16x32
from cam.CamSetup import SetupFun
from cam.CamShoot import ShootFun
from config.io import *

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
            ShootFun(Shoot, TimeShoot, TimeBtween, ShootCount, tft)
            Shoot = False
            string = 'Dokonceno              '
            tft.text(vga_16x32, string, 10, 100)
            sleep(2)
        
except KeyboardInterrupt:
    # This part runs when Ctrl+C is pressed
    print("Program stopped. Exiting...")

    # Optional cleanup code
        







