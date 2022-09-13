"""a"""
from multiprocessing.connection import wait
from platform import win32_edition
from time import sleep
from turtle import st
from asr.gcloud import GCloud
from asr.lvosk import Vosk
from microphone.microphone import MicrophoneStream
import os

RATE = 16000
CHUNK = int(RATE / 10)

def main():
    """a"""
    auth_path = os.path.realpath("gcloud-key.json")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = auth_path

    with MicrophoneStream(RATE, CHUNK) as stream:
        while not stream.closed:

            # gcloud = GCloud("pt-BR", RATE)

            # result = gcloud.next(stream)

            vosk = Vosk(rate=RATE)

            result = vosk.next(stream)

            print(result)


def test():
    import pywinctl as pwc
    import subprocess
    # import json
    from pywinctl import Win32Window
    import pyautogui

    subprocess.Popen('notepad')
    sleep(0.5)
    windows = pwc.getWindowsWithTitle('bloco de notas', condition=pwc.Re.CONTAINS, flags=pwc.Re.IGNORECASE)
    # print(pwc.getAllTitles())
    # print(windows)
    if windows:
        win : Win32Window = windows[0]
        # menu = win.menu.getMenu()
        # print(json.dumps(menu, indent=4, ensure_ascii=False))  # Prints menu dict in legible format
        # ret = win.menu.clickMenuItem(["File", "Exit"])           # Exit program
        # if not ret:
            # print("Option not found. Check option path and language")

        im = pyautogui.screenshot("banana.png", region=win.box)
        print(win.topright, win.topleft, win.top, win.width, win.height, win.box)
        print(im)
    else:
        print("Window not found. Check application name and language")

if __name__ == "__main__":
    # main()
    test()
