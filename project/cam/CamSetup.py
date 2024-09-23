# část kódu pro nastavení parametrů
import time
from machine import Pin, SPI
from disp import st7789
from disp import vga_16x32

#input definition
btnEnter = Pin(27, Pin.IN, Pin.PULL_DOWN)
btnDwnS  = Pin(26, Pin.IN, Pin.PULL_DOWN)
btnUpS   = Pin(25, Pin.IN, Pin.PULL_DOWN)
btnDwnDec= Pin(15, Pin.IN, Pin.PULL_DOWN)
btnUpDec = Pin(12, Pin.IN, Pin.PULL_DOWN)

def SetupFun(Setup, TimeShoot, TimeBtween, ShootCount, tft):
    # globální proměnná tlačítek
    global btnEnter
    global btnDwnS
    global btnUpS
    global btnDwnDec
    global btnUpDec
    #global tft
    # definice základního nastavení
    Step = 0
    TempStep = 1
    ChangeParams = True
    ShootNow = True
    String = ""
    PrevString = ""
    PrevTimeShoot = 0
    PrevTimeBtween = 0
    PrevShootCount = 0
    # oznaceni tlacitek
    # desetinova tlacitka
    tft.text(vga_16x32, '^', 70, 5)
    tft.text(vga_16x32, 'v', 70, 200)
    tft.text(vga_16x32, '+', 70, 15)
    tft.text(vga_16x32, 's', 70, 40)
    # vterinova tlacitka
    tft.text(vga_16x32, '^', 240, 5)
    tft.text(vga_16x32, 'v', 240, 200)
    tft.text(vga_16x32, '+', 240, 15)
    tft.text(vga_16x32, 's/10', 220, 40)
    
    while ( Setup == True ):
       if ( Step == 0 ):
           if ( TimeShoot > 0 ) and ( TimeBtween > 0 ) and ( ShootCount > 0 ):
               # zeptat se zda změnit parametry
               if ( btnUpS.value() == True ) or ( btnDwnS.value() == True ):
                   ChangeParams = not (ChangeParams)
                   time.sleep(0.5)
               if ( ChangeParams == True ):
                   String = "Zmenit param: Ano       "
               else:
                   String = "Zmenit param: Ne        "  
               if ( btnEnter.value() == True ) and ( ChangeParams == True ):
                   Step = 1
                   time.sleep(0.5)
               elif ( btnEnter.value() == True ) and ( ChangeParams == False ):
                   Step = 5
                   time.sleep(0.5)
           else:
               Step = 1 
       elif ( Step == 1 ):
           # nastavíme první čas
           if ( btnUpS.value() == True ):
               TimeShoot += 1
               time.sleep(0.5)
                   
           if ( btnDwnS.value() == True ) and ( TimeShoot >= 1 ):
               TimeShoot -= 1
               time.sleep(0.5)
                   
           if ( btnUpDec.value() == True ):
               TimeShoot += 0.1
               time.sleep(0.5)  
           if ( btnDwnDec.value() == True ) and ( TimeShoot > 0 ):
               TimeShoot -= 0.1
               time.sleep(0.5)  
           if ( btnEnter.value() == True ) and ( TimeShoot > 0):
               time.sleep(0.5)
               Step = 2
           String = "Cas zaverky: " + str(TimeShoot) + " s        " 
       elif ( Step == 2 ):
           # nastavíme druhý čas
           if ( btnUpS.value() == True ):
               TimeBtween += 1
               time.sleep(0.5)
                   
           if ( btnDwnS.value() == True ) and ( TimeBtween >= 1 ):
               TimeBtween -= 1
               time.sleep(0.5)
                   
           if ( btnUpDec.value() == True ):
               TimeBtween += 0.1
               time.sleep(0.5)  
           if ( btnDwnDec.value() == True ) and ( TimeBtween > 0 ):
               TimeBtween -= 0.1
               time.sleep(0.5)  
           if ( btnEnter.value() == True ) and ( TimeBtween > 0 ):
               time.sleep(0.5)
               Step = 3
           String = "Cas mezi sn.: " + str(TimeBtween) + " s       " 
       elif ( Step == 3 ):
           # nastavíme počet fotek
           if ( btnUpS.value() == True ):
               ShootCount += 1
               time.sleep(0.5)
                   
           if ( btnDwnS.value() == True ) and ( ShootCount >= 1 ):
               ShootCount -= 1
               time.sleep(0.5)  
           if ( btnEnter.value() == True ) and ( ShootCount > 0 ):
               String = "Revize nastaveni"
               time.sleep(0.5)
               Step = 4
           String = "Pocet snimku: " + str(ShootCount) + "        "   
       elif (Step == 4 ):
           # zrevidujeme časy
           if ( btnUpS.value() == True ):
               if ( TempStep < 4 ):
                   TempStep += 1                           # inkrementujeme krok do limitu 4
               else:
                   TempStep = 1                            # při pokusu inkrementovat nad dáme 1
               time.sleep(0.5)
               
           if ( btnDwnS.value() == True ):
               if ( TempStep <= 1 ):
                   TempStep = 4                            # při pokusu dekrementovat krok pod limit 1 dáme 4
               else:
                   TempStep -= 1                            # dekrementujeme jinak krok
               time.sleep(0.5)
               
           if ( TempStep == 1 ):
               String = 'Nast. cas zaverky        '         # přiřadíme texty
           elif ( TempStep == 2 ):
               String = 'Nast. cas mezi sn.       '
           elif ( TempStep == 3 ):
               String = 'Nast. pocet sn.          '
           else:
               String = 'Pokracovat               '
               
           if ( btnEnter.value() == True ):
               if ( TempStep == 4 ):
                   Step = 5
               else:
                   Step = TempStep
               time.sleep(0.5)
       elif ( Step == 5 ):
           # zeptat se zda rovnou fotit
           if ( btnUpS.value() == True ) or ( btnDwnS.value() == True):
               ShootNow = not( ShootNow )
               time.sleep(0.5)
           if ( ShootNow == True ):
               String = "Zacit foceni: Ano         "
           else:
               String = "Zacit foceni: Ne          "  
           if ( btnEnter.value() == True ) and ( ShootNow == True ):
               Shoot = True
               Setup = False
           elif ( btnEnter.value() == True ) and ( ShootNow == False ):
               Shoot = False
               Setup = False    
       else:
           Setup = False
           Shoot = False
           Step = 0
    
       if ( PrevString != String ):
            # zapsat nový string
            tft.text(vga_16x32, String, 10, 100)
            PrevString = String
           
       if ( PrevTimeShoot != TimeShoot ):
           # zapsat nový čas focení
           tft.text(vga_16x32, str(TimeShoot) + " s   ", 30, 170)
           PrevTimeShoot = TimeShoot
           
       if ( PrevTimeBtween != TimeBtween ):
           # zapsat nový čas mezi fotkami
           tft.text(vga_16x32, str(TimeBtween) + " s   ", 150, 170)
           PrevTimeBtween = TimeBtween
           
       if ( PrevShootCount != ShootCount ):
           # zapsat nový počet snímků
           tft.text(vga_16x32, str(ShootCount) + " x   ", 260, 170)
           PrevShootCount = ShootCount
    
    Step = 0
    
    # smazani popisu tlacitek
    # Vterinova tlacitka
    tft.text(vga_16x32, '  ', 70, 5)
    tft.text(vga_16x32, '  ', 70, 200)
    tft.text(vga_16x32, '  ', 70, 15)
    tft.text(vga_16x32, '  ', 70, 40)
    # desetinna tlacitka
    tft.text(vga_16x32, '  ', 240, 5)
    tft.text(vga_16x32, '  ', 240, 200)
    tft.text(vga_16x32, '  ', 240, 15)
    tft.text(vga_16x32, '    ', 220, 40)
    
    ToReturn = [TimeShoot, TimeBtween, ShootCount, Shoot]
    return ToReturn

