


def isVsync(settingChoice, windowName):
    if settingChoice == 'True':
        windowName.vsync = True

    if settingChoice == 'False':
        windowName.vsync = False