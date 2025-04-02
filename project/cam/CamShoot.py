# část kódu pro focení
import time
from disp import vga_16x32
from config.io import *
from cam.functions import *


def ShootFun(Shoot, TimeShoot, TimeBtween, ShootCount, tft, ptpip, wlanActive):
    while ( Shoot == True ):
        string = 'Zbyva: ' + str((ShootCount-1)) + '    '
        tft.text(vga_16x32, string, 10, 20)
        #outCamShoot.on()
        #time.sleep(TimeShoot)
        #outCamShoot.off()
        if ( wlanActive == True ):
            ptpipShutter(ptpip, TimeShoot)
        else:
            wiredShutter(TimeShoot)
        time.sleep(TimeBtween)
        if ( ShootCount > 1):
            ShootCount -= 1
        else:
            string = '                       '
            tft.text(vga_16x32, string, 10, 20)
            Shoot = False
    return

    
