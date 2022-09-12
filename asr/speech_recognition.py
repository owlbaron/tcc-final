"""Esse modulo conterá todas as implementações para reconhecimento de fala."""

class SpeechRecognition:
    """Essa classe é uma interface para serviços de reconhecimento de fala."""

    def next(self, stream) -> str:
        """Retorna o próximo resultado reconhecido."""
        raise NotImplementedError
