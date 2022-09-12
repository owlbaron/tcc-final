"""Implementação para reconhecimento de fala usando a biblioteca Vosk."""
import json
from vosk import Model, KaldiRecognizer
from speech_recognition import SpeechRecognition


class Vosk(SpeechRecognition):
    """Essa classe é a implementação de reconhecimento de fala com a biblioteca Vosk."""

    def __init__(self, rate) -> None:
        model = Model(r'C:/Users/barao/dev/senac/tcc/poc-vosk/model-4')
        self.recognizer = KaldiRecognizer(model, rate)
        pass

    def next(self, stream) -> str:
        """Retorna o próximo resultado reconhecido."""
        audio_generator = stream.generator()

        for content in audio_generator:
            if self.recognizer.AcceptWaveform(content):
                result = self.recognizer.Result()

                result_dict = json.loads(result)

                return result_dict.get("text", "")
        