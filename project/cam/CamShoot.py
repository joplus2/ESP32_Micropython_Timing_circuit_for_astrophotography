# část kódu pro focení
import time
from disp import vga_16x32
from config.io import *


def ShootFun(Shoot, TimeShoot, TimeBtween, ShootCount, tft):
    while ( Shoot == True ):
        string = 'Zbyva: ' + str((ShootCount-1))
        tft.text(vga_16x32, string, 10, 40)
        outCamShoot.on()
        time.sleep(TimeShoot)
        outCamShoot.off()
        time.sleep(TimeBtween)
        if ( ShootCount > 1):
            ShootCount -= 1
        else:
            string = '                       '
            tft.text(vga_16x32, string, 10, 40)
            Shoot = False
    return

    
