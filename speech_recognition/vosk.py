"""Implementação para reconhecimento de fala usando a biblioteca Vosk."""
from speech_recognition import SpeechRecognition

# from vosk import Model, KaldiRecognizer
# import pyaudio

# model = Model(r'C:/Users/barao/dev/senac/tcc/poc-vosk/model-4')
# recognizer = KaldiRecognizer(model, 16000)

# cap = pyaudio.PyAudio()
# stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
# stream.start_stream()

# while True:
#     data = stream.read(4096)
#     if recognizer.AcceptWaveform(data):
#         print(recognizer.Result())


class Vosk(SpeechRecognition):
    """Essa classe é a implementação de reconhecimento de fala com a biblioteca Vosk."""

    def __init__(self) -> None:
        #model = Model(r'C:/Users/barao/dev/senac/tcc/poc-vosk/model-4')
        #recognizer = KaldiRecognizer(model, 16000)
        # cap = pyaudio.PyAudio()
        # stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
        pass

    def start(self) -> None:
        """Inicia o buffer de leitura e fecha o microfone"""

    def stop(self) -> None:
        """Finaliza o buffer de leitura e fecha o microfone"""
        # stream.end/close?
        # cap.close?

    def next(self) -> str:
        """Retorna o próximo resultado reconhecido."""
        # data = stream.read(4096)
        #     if recognizer.AcceptWaveform(data):
        #         print(recognizer.Result())
        