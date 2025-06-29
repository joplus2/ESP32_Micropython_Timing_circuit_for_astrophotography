# shooting function
import time
from disp import vga_16x32
from config.io import *
from cam.functions import *
from config.battery import battMeasure


def ShootFun(Shoot, TimeShoot, TimeBtween, ShootCount, tft, ptpip, wlanActive):
    while ( Shoot == True ):
        string = 'Zbyva: ' + str((ShootCount-1)) + '    '
        tft.text(vga_16x32, string, 10, 20)
        battMeasure(tft)
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

    
