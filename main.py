"""a"""
from multiprocessing.connection import wait
from platform import win32_edition
from time import sleep
from asr.gcloud import GCloud
from asr.lvosk import Vosk
from microphone.microphone import MicrophoneStream
import os
from cvmodel.yolo_ovj_dection import DarknetModel

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
    import pyautogui

    subprocess.Popen('mgba-qt')
    sleep(1)
    windows = pwc.getWindowsWithTitle('mgba', condition=pwc.Re.CONTAINS, flags=pwc.Re.IGNORECASE)
    # print(pwc.getAllTitles())
    # print(windows)
    if windows:
        win : pwc.Window = windows[0]
        # menu = win.menu.getMenu()
        # print(json.dumps(menu, indent=4, ensure_ascii=False))  # Prints menu dict in legible format
        # ret = win.menu.clickMenuItem(["File", "Exit"])           # Exit program
        # if not ret:
            # print("Option not found. Check option path and language")

        im = pyautogui.screenshot(None, region=win.box)
        print(win.topright, win.topleft, win.top, win.width, win.height, win.box)
        print(im)
    else:
        print("Window not found. Check application name and language")

def model():
    darknet_model = DarknetModel(
        cfg_path= "/home/miyamoto/projects/tcc/darknet/nosso-yolo/yolov4-obj.cfg", 
        weights_path= "/home/miyamoto/projects/tcc/darknet/nosso-yolo/data/backup/yolov4-obj_best.weights",
        classes_name= ["battle", "exploration", "menu"]
    )

    darknet_model.detect("/home/miyamoto/projects/tcc/darknet/nosso-yolo/dataset/va/batalha19442_png.rf.973db3164f20398879f2090e2ed3e412.jpg")

if __name__ == "__main__":
    # main()
    # test()
    model()

#####

# No Manjaro (KDE) tava dando esse erro

# QObject::moveToThread: Current thread (...) is not the object's thread (...).
# Cannot move to target thread (...)
# qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "/(...)site-packages/cv2/qt/plugins" even though it was found.
# This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.


# jeito que funcionou, foi a ultima resposta do link, aparentemente como o opencv trata alguma coisa
# instalar o opencv headless
#https://github.com/NVlabs/instant-ngp/discussions/300