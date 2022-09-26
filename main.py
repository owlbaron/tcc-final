"""Arquivo principal, o que deve ser executado."""
from time import sleep
import pywinctl as pwc
import pyautogui
from asr.gcloud import GCloud
from microphone.microphone import MicrophoneStream
from multiprocessing import Process
import os
from cvmodel.yolo_obj_dection import DarknetModel
from vision.state_writer import StateWriter

RATE = 16000
CHUNK = int(RATE / 10)

def init_main():
    """Incializador da entrada por voz"""
    command_map = {
        "cima": "up",
        "baixo": "down",
        "esquerda": "left",
        "direita": "right"
    }

    gcloud = GCloud(language="pt-BR", rate=RATE)

    with MicrophoneStream(RATE, CHUNK) as stream:
        while not stream.closed:
            result = gcloud.next(stream)

            result_after_processing = result.lower()

            if result_after_processing in command_map:
                pyautogui.press(command_map[result_after_processing])
            else:
                pyautogui.alert(
                    text=f"O comando \"{result_after_processing}\" é desconhecido.",
                    title='Comando desconhecido',
                    button='OK',
                )

def init_feeder():
    """Inicializador do Modelo"""
    state_writer = StateWriter()
    darknet_model = DarknetModel(
        cfg_path= "/home/miyamoto/projects/tcc/darknet/nosso-yolo/yolov4-obj.cfg", 
        weights_path= "/home/miyamoto/projects/tcc/darknet/nosso-yolo/data/backup/yolov4-obj_best.weights",
        classes_name= ["attack-change-menu","bag-menu","battle","exploration","fight-attack-menu","fight-bag-menu","fight-main-menu","indicator","map","menu","poke-center-menu","pokemon-selection","yes-no-menu"]
    )

    # subprocess.Popen('mgba-qt')
    sleep(1)
    windows = pwc.getWindowsWithTitle('mgba', condition=pwc.Re.CONTAINS, flags=pwc.Re.IGNORECASE)

    if windows:
        win : pwc.Window = windows[0]

        win.maximize()

        while True:
            sleep(5)
            if not win.isMinimized:
                win.restore()

            im = pyautogui.screenshot(None, region=win.box)

            result = darknet_model.detect(im)

            state_writer.write_result(result)

def main():
    """Função Principal, responsável por executar os diferente módulos e integrá-los"""

    auth_path = os.path.realpath("gcloud-key.json")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = auth_path

    # io = Process(target=init_main)
    feeder = Process(target=init_feeder)

    # io.start()
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
