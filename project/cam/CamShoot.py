# část kódu pro focení
import time
from machine import Pin

pinOut = Pin(23, Pin.OUT)

def ShootFun(Shoot, TimeShoot, TimeBtween, ShootCount):
    global pinOut
    while ( Shoot == True ):
        pinOut.on()
        time.sleep(TimeShoot)
        pinOut.off()
        time.sleep(TimeBtween)
        if ( ShootCount > 1):
            ShootCount -= 1
        else:
            Shoot = False
    return

    
