# file with display functions
from disp import vga_16x32
from disp import st7789


# initial vars state
PrevString = ""
PrevTimeShoot = 0
PrevTimeBtween = 0
PrevShootCount = 0

def showSecondBtns(tft):
    tft.text(vga_16x32, '^', 70, 5)
    tft.text(vga_16x32, 'v', 70, 200)
    tft.text(vga_16x32, '+', 70, 15)
    #tft.text(vga_16x32, 's', 70, 40)
    
def showDecimalBtns(tft):
    tft.text(vga_16x32, '^', 240, 5)
    tft.text(vga_16x32, 'v', 240, 200)
    tft.text(vga_16x32, '+', 240, 15)
    #tft.text(vga_16x32, 's/10', 220, 40)
    
def vanishSecBtns(tft):
    tft.text(vga_16x32, '  ', 70, 5)
    tft.text(vga_16x32, '  ', 70, 200)
    tft.text(vga_16x32, '  ', 70, 15)
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
        tft.text(vga_16x32, str(TimeShoot) + " s   ", 30, 170)
        PrevTimeShoot = TimeShoot
        
def updateTimeBtween(tft, TimeBtween):
    global PrevTimeBtween
    if ( PrevTimeBtween != TimeBtween ):
        # zapsat nový čas mezi fotkami
        tft.text(vga_16x32, str(TimeBtween) + " s   ", 150, 170)
        PrevTimeBtween = TimeBtween
        
def updateShootCount(tft, ShootCount):
    global PrevShootCount
    if ( PrevShootCount != ShootCount ):
        # zapsat nový počet snímků
        tft.text(vga_16x32, str(ShootCount) + " x   ", 260, 170)
        PrevShootCount = ShootCount
        
def showTimeWarning(tft, show=True):
    if ( show ):
        # show warning, that recomended time was exceeded
        tft.text(vga_16x32, "Presazen dop. cas!", 10, 60, background=st7789.RED)
    else:
        tft.fill_rect(10, 60, 300, 32, st7789.BLACK)
        
