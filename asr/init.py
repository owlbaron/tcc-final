from asr.gcloud import GCloud
from microphone.microphone import MicrophoneStream

RATE = 16000
CHUNK = int(RATE / 10)

def init():
    with MicrophoneStream(RATE, CHUNK) as stream:
        while not stream.closed:

            gcloud = GCloud("pt-BR", RATE)

            result = gcloud.next(stream)

            # vosk = Vosk(rate=RATE)

            # result = vosk.next(stream)

            print(result)
