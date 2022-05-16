import pyautogui


def nextSong(lg):
    pyautogui.hotkey('shift', 'n')
    if lg == 'en':
        return 'Changed song'
    else:
        return "Đã chuyển bài"


def fullScreen(lg):
    pyautogui.hotkey('f')
    if lg == 'en':
        return 'Zoomed out'
    else:
        return "Đã phóng to"


def forward(lg):
    pyautogui.hotkey('right')
    if lg == 'en':
        return 'Ok boss'
    else:
        return "OK ngài"


def back(lg):
    pyautogui.hotkey('left')
    if lg == 'en':
        return 'Ok boss'
    else:
        return "OK ngài"


def pause(lg):
    pyautogui.hotkey('space')
    if lg == 'en':
        return 'Ok boss'
    else:
        return "OK ngài"


def play(lg):
    pyautogui.hotkey('space')
    if lg == 'en':
        return 'Ok boss'
    else:
        return "OK ngài"


def volumeDown(lg):
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    if lg == 'en':
        return 'Ok boss'
    else:
        return "OK ngài"


def volumeUp(lg):
    pyautogui.hotkey('up')
    pyautogui.hotkey('up')
    pyautogui.hotkey('up')
    pyautogui.hotkey('up')
    pyautogui.hotkey('up')
    if lg == 'en':
        return 'Ok boss'
    else:
        return "OK ngài"
