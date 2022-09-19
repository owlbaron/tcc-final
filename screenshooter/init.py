from time import sleep
import pywinctl as pwc
import subprocess
import pyautogui

def init():
    subprocess.Popen('mgba-qt')
    sleep(1)
    windows = pwc.getWindowsWithTitle('mgba', condition=pwc.Re.CONTAINS, flags=pwc.Re.IGNORECASE)

    if windows:
        win : pwc.Window = windows[0]

        win.maximize()

        im = pyautogui.screenshot(None, region=win.box)
        print(win.topright, win.topleft, win.top, win.width, win.height, win.box)
        print(im)
