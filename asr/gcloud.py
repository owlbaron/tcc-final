"""Implementação para reconhecimento de fala usando a API da GCloud."""
from google.cloud import speech
from asr.speech_recognition import SpeechRecognition

class GCloud(SpeechRecognition):
    """Essa classe é a implementação de reconhecimento de fala com a ferramenta da GCloud."""

    def __init__(self, language, rate) -> None:
        super().__init__()

        self.rate = rate
        self.language = language
        self.client = speech.SpeechClient()

    def next(self, stream) -> str:
        """Retorna o próximo resultado reconhecido."""
        audio_generator = stream.generator()

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=self.rate,
            language_code=self.language,
        )
        streaming_config = speech.StreamingRecognitionConfig(
            config=config, interim_results=True
        )

        # request = speech.StreamingRecognizeRequest(streaming_config=streaming_config)

        requests = (
            speech.StreamingRecognizeRequest(audio_content=content)
            for content in audio_generator
        )

        # requests.insert(0, request)

        responses = self.client.streaming_recognize(
            streaming_config,
            requests,
        )

        for response in responses:
            if not response.results:
                continue

            # The `results` list is consecutive. For streaming, we only care about
            # the first result being considered, since once it's `is_final`, it
            # moves on to considering the next utterance.
            result = response.results[0]
            if not result.alternatives:
                continue

            # Display the transcription of the top alternative.
            transcript = result.alternatives[0].transcript

            if result.is_final:
                return transcript

        return ""
