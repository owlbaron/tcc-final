"""a"""
from time import sleep
import pywinctl as pwc
import subprocess
from pywinctl import Win32Window
import pyautogui
from asr.gcloud import GCloud
from microphone.microphone import MicrophoneStream
from multiprocessing import Process
import os
from cvmodel.yolo_obj_dection import DarknetModel

RATE = 16000
CHUNK = int(RATE / 10)

def initMain(model):
    map = {
        "cima": "up",
        "baixo": "down",
        "esquerda": "left",
        "direita": "right"
    }

    gcloud = GCloud(language="pt-BR", rate=RATE)

    with MicrophoneStream(RATE, CHUNK) as stream:
        while not stream.closed:
            result = gcloud.next(stream)

            if result in map:
                pyautogui.press(map[result])
            else:
                pyautogui.alert(text=f"O comando \"{result}\" é desconhecido ", title='Comando desconhecido', button='OK')

def initFeeder(model):  
    subprocess.Popen('notepad')
    sleep(0.5)
    windows = pwc.getWindowsWithTitle('bloco de notas', condition=pwc.Re.CONTAINS, flags=pwc.Re.IGNORECASE)

    if windows:
        win : Win32Window = windows[0]

        win.maximize()

        while True:
            sleep(0.1)
            im = pyautogui.screenshot(None, region=win.box)

            model.detect(im)



def main():
    """a"""
    darknet_model = DarknetModel(
        cfg_path= "/home/miyamoto/projects/tcc/darknet/nosso-yolo/yolov4-obj.cfg", 
        weights_path= "/home/miyamoto/projects/tcc/darknet/nosso-yolo/data/backup/yolov4-obj_best.weights",
        classes_name= ["battle", "exploration", "menu"]
    )

    auth_path = os.path.realpath("gcloud-key.json")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = auth_path

    main = Process(target=initMain, args=(darknet_model))
    feeder = Process(target=initFeeder, args=(darknet_model))

    main.start()
    feeder.start()


if __name__ == "__main__":
    main()

#####

# No Manjaro (KDE) tava dando esse erro

# QObject::moveToThread: Current thread (...) is not the object's thread (...).
# Cannot move to target thread (...)
# qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "/(...)site-packages/cv2/qt/plugins" even though it was found.
# This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.


# jeito que funcionou, foi a ultima resposta do link, aparentemente como o opencv trata alguma coisa
# instalar o opencv headless
#https://github.com/NVlabs/instant-ngp/discussions/300