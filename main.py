"""a"""
import asr.init as asr
import screenshooter.init as ss
import cvmodel.init as model
from multiprocessing import Process
import os


def main():
    """a"""
    auth_path = os.path.realpath("gcloud-key.json")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = auth_path

    pASR = Process(target=asr.init)
    pScreenshooter = Process(target=ss.init)
    pModel = Process(target=model.init)

    pASR.start()
    pScreenshooter.start()
    pModel.start()


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