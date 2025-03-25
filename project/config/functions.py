""" settings related functions """

def settingsConv(settings):
    """ current structure: WiFi(bool)-SSID(str)-Pass(str) """
    settingsTuple = [True,'CamSSID','CamPass']
    settings = settings.split("-")
    for i in range(0,len(settings)):
        if settings[i] == "0" or settings[i] == "1":
            settingsTuple[i] = bool(int(settings[i]))
        else:
            settingsTuple[i] = settings[i]
    return settingsTuple

def makeSettingString(active, SSID, password):
    return (str(int(active)) + "-" + str(SSID) + "-" + str(password))
