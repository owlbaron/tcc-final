"""Esse modulo conterá todas as implementações para reconhecimento de fala."""

class SpeechRecognition:
    """Essa classe é uma interface para serviços de reconhecimento de fala."""

    def start(self) -> None:
        """Começa a captar o audio."""
        raise NotImplementedError

    def stop(self) -> None:
        """Para de captar o audio"""
        raise NotImplementedError

    def next(self) -> str:
        """Retorna o próximo resultado reconhecido."""
        raise NotImplementedError
