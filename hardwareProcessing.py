import ctypes
import sys
import pyautogui
import winshell
import os


def open_application(lg, text):
    if "word" in text:
        os.startfile('C:/Program Files/Microsoft Office/Office15/WINWORD.EXE')
        if lg == 'en':
            return "Opening Microsoft Word"
        else:
            return "Đang mở Microsoft Word"

    elif "excel" in text:
        os.startfile('C:/Program Files/Microsoft Office/Office15/EXCEL.EXE')
        if lg == 'en':
            return "Opening Microsoft Excel"
        else:
            return "Đang mở Microsoft Excel"

    elif "one note" in text:
        os.startfile('C:/Program Files/Microsoft Office/Office15/ONENOTE.EXE')
        if lg == 'en':
            return "Opening One Note"
        else:
            return "Đang mở One Note"

    elif "out look" in text:
        os.startfile('C:/Program Files/Microsoft Office/Office15/OUTLOOK.EXE')
        if lg == 'en':
            return "Opening Out Look"
        else:
            return "Đang mở Out Look"

    elif "power point" in text:
        os.startfile('C:/Program Files/Microsoft Office/Office15/POWERPNT.EXE')
        if lg == 'en':
            return "Opening Power Point"
        else:
            return "Đang mở Power Point"

    else:
        if lg == 'en':
            return "App hasn't been inserted. Please try again"
        else:
            return "Ứng dụng chưa được cài đặt. Bạn hãy thử lại!"


def lockPC(lg):
    ctypes.windll.user32.LockWorkStation()
    if lg == 'en':
        return 'Locking Computer'
    else:
        return 'Đang khóa máy'


def shutDown(lg):
    if sys.platform == 'win32':
        user32 = ctypes.WinDLL('user32')
        user32.ExitWindowsEx(0x00000008, 0x00000000)
    else:
        os.system('Sudo shutdown now')
    os.system('shutdown /p /f')
    if lg == 'en':
        return 'Computer is shutting down'
    else:
        return 'Đang tắt máy'


def restart(lg):
    os.system('shutdown /r /f')
    if lg == 'en':
        return 'Computer is Restarting'
    else:
        return 'Đang khởi động lại'


def emptyRecyclebin(lg):
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        if lg == 'en':
            return 'Done'
        else:
            return 'Đã làm sạch thùng rác'
    except:
        if lg == 'en':
            return 'Empty recycle'
        else:
            return 'Thùng rác trống'

def closeApp(lg):
    pyautogui.hotkey('alt', 'f4')
    if lg == "en":
        return "The application is closed"
    else:
        return "Ứng dụng đã đóng"
