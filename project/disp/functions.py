# file with display functions
from disp import vga_16x32
from disp import st7789


# initial vars state
PrevString = ""
PrevTimeShoot = 0
PrevTimeBtween = 0
PrevShootCount = 0

def showEnterBtn(tft):
    tft.text(vga_16x32, '>', 270, 200)
    
def vanishEnterBtn(tft):
    tft.text(vga_16x32, '  ', 270, 200)

def showSecondBtns(tft):
    tft.text(vga_16x32, '^', 105, 5)
    tft.text(vga_16x32, 'v', 105, 200)
    tft.text(vga_16x32, '+', 105, 15)
    #tft.text(vga_16x32, 's', 70, 40)
    
def showDecimalBtns(tft):
    tft.text(vga_16x32, '^', 240, 5)
    tft.text(vga_16x32, 'v', 240, 200)
    tft.text(vga_16x32, '+', 240, 15)
    #tft.text(vga_16x32, 's/10', 220, 40)
    
def vanishSecBtns(tft):
    tft.text(vga_16x32, '  ', 105, 5)
    tft.text(vga_16x32, '  ', 105, 200)
    tft.text(vga_16x32, '  ', 105, 15)
    #tft.text(vga_16x32, '  ', 70, 40)
    
def vanishDecBtns(tft):
    tft.text(vga_16x32, '  ', 240, 5)
    tft.text(vga_16x32, '  ', 240, 200)
    tft.text(vga_16x32, '  ', 240, 15)
    #tft.text(vga_16x32, '    ', 220, 40)
    
def updateString(tft, String):
    global PrevString
    if ( PrevString != String ):
        # zapsat nový string
        tft.text(vga_16x32, String, 10, 100)
        PrevString = String
    
def updateTimeShoot(tft, TimeShoot):
    global PrevTimeShoot
    if ( PrevTimeShoot != TimeShoot ):
        # zapsat nový čas focení
        if ( TimeShoot >= 60 ):
            TempTimeShoot = int(TimeShoot/60)
            TimeShootSuffix = " m "
        else:
            TempTimeShoot = int(TimeShoot)
            TimeShootSuffix = " s "
        tft.text(vga_16x32, str(TempTimeShoot) + TimeShootSuffix, 30, 170)
        PrevTimeShoot = TimeShoot
        
def updateTimeBtween(tft, TimeBtween):
    global PrevTimeBtween
    if ( PrevTimeBtween != TimeBtween ):
        # zapsat nový čas mezi fotkami
        tft.text(vga_16x32, str(TimeBtween) + " s", 130, 170)
        PrevTimeBtween = TimeBtween
        
def updateShootCount(tft, ShootCount):
    global PrevShootCount
    if ( PrevShootCount != ShootCount ):
        # zapsat nový počet snímků
        tft.text(vga_16x32, str(ShootCount) + " x   ", 240, 170)
        PrevShootCount = ShootCount
        
def showTimeWarning(tft, show=True):
    if ( show ):
        # show warning, that recomended time was exceeded
        tft.text(vga_16x32, "Presazen dop. cas!", 10, 60, background=st7789.RED)
    else:
        tft.fill_rect(10, 60, 300, 32, st7789.BLACK)
        
