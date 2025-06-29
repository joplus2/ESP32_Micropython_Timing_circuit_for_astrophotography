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
    btnDelay = 0.25
    # show seconds button description
    showSecondBtns(tft)
    
    while ( Setup == True ):
       if ( Step == 0 ):
           if ( TimeShoot > 0 ) and ( TimeBtween > 0 ) and ( ShootCount > 0 ):
               # ask if parameters want to be changed
               if ( btnUpS.value() == False ) or ( btnDwnS.value() == False ):
                   ChangeParams = not (ChangeParams)
                   time.sleep(btnDelay)
               if ( ChangeParams == True ):
                   String = "Zmenit param: Ano       "
               else:
                   String = "Zmenit param: Ne        "  
               if ( btnEnter.value() == False ) and ( ChangeParams == True ):
                   Step = 1
                   time.sleep(btnDelay)
               elif ( btnEnter.value() == False ) and ( ChangeParams == False ):
                   Step = 5
                   time.sleep(btnDelay)
           else:
               Step = 1 
               
       elif ( Step == 1 ):
           # set up first parameter - shooting time
           if ( btnUpS.value() == False ):
               if (TimeShoot < 10):
                   TimeShoot += 1
               elif (TimeShoot < 30):
                   TimeShoot += 5
               elif (TimeShoot < 60):
                   TimeShoot += 10
               else:
                   TimeShoot += 60
               time.sleep(btnDelay)
           if ( btnDwnS.value() == False ) and ( TimeShoot >= 1 ):
               if (TimeShoot <= 10):
                   TimeShoot -= 1
               elif (TimeShoot <= 30):
                   TimeShoot -= 5
               elif (TimeShoot <= 60):
                   TimeShoot -= 10
               else:
                   TimeShoot -= 60
               time.sleep(btnDelay)
           if ( btnEnter.value() == False ) and ( TimeShoot > 0):
               time.sleep(0.5)
               Step = 2
           if (TimeShoot >= 60):
               String = "Cas zaverky: " + str(int(TimeShoot/60)) + " min        "
           else:
               String = "Cas zaverky: " + str(TimeShoot) + " s        " 
               
       elif ( Step == 2 ):
           # set up second parameter - time between shots
           if ( btnUpS.value() == False ):
               TimeBtween += 0.1
               time.sleep(btnDelay)
           if ( btnDwnS.value() == False ) and ( TimeBtween > 0 ):
               TimeBtween -= 0.1
               time.sleep(btnDelay)
           TimeBtween = round(TimeBtween,1)
           if ( btnEnter.value() == False ) and ( TimeBtween > 0 ):
               time.sleep(btnDelay)
               Step = 3
           if (TimeBtween > 1 ):
               showTimeWarning(tft)
           else:
               showTimeWarning(tft, False)
           String = "Cas mezi sn.: " + str(TimeBtween) + " s       " 
           
       elif ( Step == 3 ):
           # set up third parameter - count of shots
           if ( btnUpS.value() == False ):
               ShootCount += 1
               time.sleep(btnDelay)
           if ( btnDwnS.value() == False ) and ( ShootCount >= 1 ):
               ShootCount -= 1
               time.sleep(btnDelay)  
           if ( btnEnter.value() == False ) and ( ShootCount > 0 ):
               String = "Revize nastaveni"
               time.sleep(btnDelay)
               Step = 4
           String = "Pocet snimku: " + str(ShootCount) + "        "   
           
       elif (Step == 4 ):
           # revision of parameters
           if ( btnUpS.value() == False ):
               if ( TempStep < 4 ):
                   TempStep += 1                           # increment step number to limit of 4
               else:
                   TempStep = 1                            # if increment above, step 1
               time.sleep(btnDelay)
               
           if ( btnDwnS.value() == False ):
               if ( TempStep <= 1 ):
                   TempStep = 4                            # if decrement under 1 step 4
               else:
                   TempStep -= 1                            # decrement step number
               time.sleep(btnDelay)
               
           if ( TempStep == 1 ):
               String = 'Nast. cas zaverky        '         # selection of display text
           elif ( TempStep == 2 ):
               String = 'Nast. cas mezi sn.       '
           elif ( TempStep == 3 ):
               String = 'Nast. pocet sn.          '
           else:
               String = 'Pokracovat               '
               
           if ( btnEnter.value() == False ):
               if ( TempStep == 4 ):
                   Step = 5
               else:
                   Step = TempStep
               time.sleep(btnDelay)
               
       elif ( Step == 5 ):
           # ask if start photo shoot
           if ( btnUpS.value() == False ) or ( btnDwnS.value() == False):
               ShootNow = not( ShootNow )
               time.sleep(btnDelay)
           if ( ShootNow == True ):
               String = "Zacit foceni: Ano         "
           else:
               String = "Zacit foceni: Ne          "  
           if ( btnEnter.value() == False ) and ( ShootNow == True ):
               Shoot = True
               Setup = False
           elif ( btnEnter.value() == False ) and ( ShootNow == False ):
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
