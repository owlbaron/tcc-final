"""a"""
from asr.gcloud import GCloud
from microphone.microphone import MicrophoneStream

RATE = 16000
CHUNK = int(RATE / 10)

def main():
    """a"""
    with MicrophoneStream(RATE, CHUNK) as stream:
        gcloud = GCloud("pt-BR", RATE)

        result = gcloud.next(stream)

        print(result)


if __name__ == "__main__":
    main()
