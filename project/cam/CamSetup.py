# část kódu pro nastavení parametrů
import time
from machine import Pin
from disp import st7789
from disp import vga_16x32
from config.io import *
from disp.functions import *


def SetupFun(Setup, TimeShoot, TimeBtween, ShootCount, tft):
    # definition of base settings
    Step = 0
    TempStep = 1
    ChangeParams = True
    ShootNow = True
    String = ""
    PrevString = ""
    PrevTimeShoot = 0
    PrevTimeBtween = 0
    PrevShootCount = 0
    # show seconds button description
    showSecondBtns(tft)
    
    while ( Setup == True ):
       if ( Step == 0 ):
           if ( TimeShoot > 0 ) and ( TimeBtween > 0 ) and ( ShootCount > 0 ):
               # ask if parameters want to be changed
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
           # set up first parameter - shooting time
           if ( btnUpS.value() == True ):
               if (TimeShoot < 10):
                   TimeShoot += 1
               elif (TimeShoot < 30):
                   TimeShoot += 5
               elif (TimeShoot < 60):
                   TimeShoot += 10
               else:
                   TimeShoot += 60
               time.sleep(0.5)
           if ( btnDwnS.value() == True ) and ( TimeShoot >= 1 ):
               if (TimeShoot <= 10):
                   TimeShoot -= 1
               elif (TimeShoot <= 30):
                   TimeShoot -= 5
               elif (TimeShoot <= 60):
                   TimeShoot -= 10
               else:
                   TimeShoot -= 60
               time.sleep(0.5)
           if ( btnEnter.value() == True ) and ( TimeShoot > 0):
               time.sleep(0.5)
               Step = 2
           if (TimeShoot >= 60):
               String = "Cas zaverky: " + str(int(TimeShoot/60)) + " min        "
           else:
               String = "Cas zaverky: " + str(TimeShoot) + " s        " 
               
       elif ( Step == 2 ):
           # set up second parameter - time between shots
           if ( btnUpS.value() == True ):
               TimeBtween += 0.1
               time.sleep(0.5)
           if ( btnDwnS.value() == True ) and ( TimeBtween > 0 ):
               TimeBtween -= 0.1
               time.sleep(0.5)
           TimeBtween = round(TimeBtween,1)
           if ( btnEnter.value() == True ) and ( TimeBtween > 0 ):
               time.sleep(0.5)
               Step = 3
           if (TimeBtween > 1 ):
               showTimeWarning(tft)
           else:
               showTimeWarning(tft, False)
           String = "Cas mezi sn.: " + str(TimeBtween) + " s       " 
           
       elif ( Step == 3 ):
           # set up third parameter - count of shots
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
           # revision of parameters
           if ( btnUpS.value() == True ):
               if ( TempStep < 4 ):
                   TempStep += 1                           # increment step number to limit of 4
               else:
                   TempStep = 1                            # if increment above, step 1
               time.sleep(0.5)
               
           if ( btnDwnS.value() == True ):
               if ( TempStep <= 1 ):
                   TempStep = 4                            # if decrement under 1 step 4
               else:
                   TempStep -= 1                            # decrement step number
               time.sleep(0.5)
               
           if ( TempStep == 1 ):
               String = 'Nast. cas zaverky        '         # selection of display text
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
           # ask if start photo shoot
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
    
       # aktualizace informaci na displeji
       updateString(tft, String)
       updateTimeShoot(tft, TimeShoot)
       updateTimeBtween(tft, TimeBtween)
       updateShootCount(tft, ShootCount)
    
    Step = 0
    
    # smazani popisu tlacitek
    # Vterinova tlacitka
    vanishSecBtns(tft)
    
    ToReturn = [TimeShoot, TimeBtween, ShootCount, Shoot]
    return ToReturn

