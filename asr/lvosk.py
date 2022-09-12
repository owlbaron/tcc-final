"""Implementação para reconhecimento de fala usando a biblioteca Vosk."""
import json
from vosk import Model, KaldiRecognizer, SetLogLevel
from asr.speech_recognition import SpeechRecognition


class Vosk(SpeechRecognition):
    """Essa classe é a implementação de reconhecimento de fala com a biblioteca Vosk."""

    def __init__(self, rate) -> None:
        dir_path = r"E:/repo/tcc-final/asr_model/vosk-model-fb"

        model = Model(dir_path)
        self.recognizer = KaldiRecognizer(model, rate)
        SetLogLevel(-1)

    def next(self, stream) -> str:
        """Retorna o próximo resultado reconhecido."""
        audio_generator = stream.generator()

        for content in audio_generator:
            if self.recognizer.AcceptWaveform(content):
                result = self.recognizer.Result()

                result_dict = json.loads(result)

                return result_dict.get("text", "")
        