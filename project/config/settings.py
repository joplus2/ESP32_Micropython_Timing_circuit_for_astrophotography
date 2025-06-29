""" Mirocontroller settings function """

import time
from machine import reset
from disp import st7789
from disp import vga_16x32
from config.io import *
from disp.functions import *
from config.functions import *

def mcuSettings(tft, prevSettings):
    tft.fill_rect(0, 100, 320, 32, st7789.BLACK)
    newSettings = [prevSettings[0], "", ""]
    Setup = True
    btnDelay = 0.10
    Step = 0
    TempStep = 0
    char = 32
    charCnt = 0
    string2 = ""
    string = ""
    string3 = ""
    showSecondBtns(tft)
    showEnterBtn(tft)
    while (Setup == True ):
        if ( Step == 0 ):
            if ( btnUpS.value() == False ) or ( btnDwnS.value() == False ):
                   newSettings[0] = not (newSettings[0])
                   time.sleep(btnDelay)
            if ( newSettings[0] == True ):
                string = "Vyuzivat WiFi: Ano    "
            else:
                string = "Vyuzivat WiFi: Ne     "
            if ( btnEnter.value() == False ):
                Step = 1
                time.sleep(btnDelay)
        
        elif ( Step == 1 ):
            """ Step for typing SSID """
            """
                ASCII to be used:
            A = 65 / Z = 90
            a = 97 / z = 122
            0 = 48 / 9 = 57
            - = 45
            _ = 95
            """
            string = "WiFi SSID:            "
            string3 = prevSettings[1]
            
            if (( btnUpS.value() == False ) or ( btnDwnS.value() == False )) and ( char == 32 ):
                   char = 65
                   time.sleep(btnDelay)
            
            if ( btnUpS.value() == False ) and ( btnDwnS.value() == True ):
                char += 1
                time.sleep(btnDelay)
            elif ( btnUpS.value() == True ) and ( btnDwnS.value() == False ):
                char -= 1
                time.sleep(btnDelay)
            elif ( btnUpS.value() == False ) and ( btnDwnS.value() == False ):
                char = 32
                time.sleep(btnDelay)
            
            # logic for typing:
            if ( char == 91 ):
                char = 97
            elif ( char == 64 ):
                char = 95
            elif ( char == 123 ):
                char = 48
            elif ( char == 96 ):
                char = 90
            elif ( char == 58 ):
                char = 45
            elif ( char == 47 ):
                char = 122
            elif ( char == 46 ):
                char = 95
            elif ( char == 44 ):
                char = 57
            elif ( char == 96 ):
                char = 65
            elif ( char == 94 ):
                char = 45
            
            string2 = newSettings[1]
            tft.text(vga_16x32, chr(char), (20+(16*charCnt)), 100)
            
            if ( btnEnter.value() == False ) and not (char == 32):
                newSettings[1] = newSettings[1] + chr(char)
                charCnt += 1
                char = 32
                time.sleep(btnDelay)
            elif ( btnEnter.value() == False ) and ( char == 32 ):
                if ( newSettings[1] == ""):
                    newSettings[1] = prevSettings[1]
                Step += 1
                charCnt = 0
                time.sleep(btnDelay)
                string2 = "                   "
                string3 = "                   "
            
        elif ( Step == 2 ):
            """ WiFi password settings """
            string = "WiFi heslo:          "
            string3 = prevSettings[2]
            
            if (( btnUpS.value() == False ) or ( btnDwnS.value() == False )) and ( char == 32 ):
                   char = 65
                   time.sleep(btnDelay)
            
            if ( btnUpS.value() == False ) and ( btnDwnS.value() == True ):
                char += 1
                time.sleep(btnDelay)
            elif ( btnUpS.value() == True ) and ( btnDwnS.value() == False ):
                char -= 1
                time.sleep(btnDelay)
            elif ( btnUpS.value() == False ) and ( btnDwnS.value() == False ):
                char = 65
                time.sleep(btnDelay)
            
            # logic for typing:
            if ( char == 91 ):
                char = 97
            elif ( char == 64 ):
                char = 95
            elif ( char == 123 ):
                char = 48
            elif ( char == 96 ):
                char = 90
            elif ( char == 58 ):
                char = 45
            elif ( char == 47 ):
                char = 122
            elif ( char == 46 ):
                char = 95
            elif ( char == 44 ):
                char = 57
            elif ( char == 96 ):
                char = 65
            elif ( char == 94 ):
                char = 45
                
            string2 = newSettings[2]
            tft.text(vga_16x32, chr(char), (20+(16*charCnt)), 100)
            
            if ( btnEnter.value() == False ) and not (char == 32):
                newSettings[2] = newSettings[2] + chr(char)
                charCnt += 1
                char = 32
                time.sleep(btnDelay)
            elif ( btnEnter.value() == False ) and ( char == 32 ):
                if ( newSettings[2] == "" ):
                    newSettings[2] = prevSettings[2]
                Step += 1
                charCnt = 0
                time.sleep(btnDelay)
                string2 = "                   "
                string3 = "                   "
            
        elif ( Step == 3 ):
           # revision
           if ( btnUpS.value() == False ):
               time.sleep(btnDelay)
               if ( TempStep < 4 ):
                   TempStep += 1                           # inkrementujeme krok do limitu 4
               else:
                   TempStep = 1                            # při pokusu inkrementovat nad dáme 1
               
           if ( btnDwnS.value() == False ):
               time.sleep(btnDelay)
               if ( TempStep <= 1 ):
                   TempStep = 4                            # při pokusu dekrementovat krok pod limit 1 dáme 4
               else:
                   TempStep -= 1                            # dekrementujeme jinak krok
               
           if ( TempStep == 0 ):
               string = 'Nast. stavu WiFi         '         # přiřadíme texty
           elif ( TempStep == 1 ):
               string = 'Nast. SSID               '
           elif ( TempStep == 2 ):
               string = 'Nast. hesla              '
           else:
               string = 'Pokracovat               '
               
           if ( btnEnter.value() == False ):
               time.sleep(btnDelay)
               if ( TempStep == 3 ):
                   Step = 4
               else:
                   Step = TempStep
               
        elif ( Step == 4 ):
            tft.text(vga_16x32, string, 20, 50, color=0xF800)
            """ Step handling and saving settings """
            stringToSave = makeSettingString(newSettings[0], newSettings[1], newSettings[2])
            f = open("/config/settings.txt", "w")
            f.write(stringToSave)
            f.close()
            time.sleep(0.5)
            reset()
            
        tft.text(vga_16x32, string, 20, 50)
        tft.text(vga_16x32, string2, 20, 100)
        tft.text(vga_16x32, string3, 20, 150)
    
