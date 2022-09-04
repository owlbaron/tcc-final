"""Implementação para reconhecimento de fala usando a API da GCloud."""
from speech_recognition import SpeechRecognition
# audio = speech.RecognitionAudio(uri=gcs_uri)

# config = speech.RecognitionConfig(
#     encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#     sample_rate_hertz=16000,
#     language_code="en-US",
# )

# # Detects speech in the audio file
# response = client.recognize(config=config, audio=audio)

# for result in response.results:
# print("Transcript: {}".format(result.alternatives[0].transcript))

class GCloud(SpeechRecognition):
    """Essa classe é a implementação de reconhecimento de fala com a ferramenta da GCloud."""

    def start(self) -> None:
        """Começa a captar o audio."""

    def stop(self) -> None:
        """Para de captar o audio"""

    def next(self) -> str:
        """Retorna o próximo resultado reconhecido."""
        