"""Módulo de leitor de estados"""
from vision.object import Object
from vision.state import State
from vision.contexts.context import Context
from vision.contexts.context_factory import ContextFactory

class StateReader:
    """
    Classe que será responsável por ler no estado.
    O objetivo com isso é que fique bem fácil de depurar e manter o código,
    além de sabermos quem está escrevendo/lendo do estado.
    """

    _state: State

    def __init__(self, state: State) -> None:
        self._state = state

    def get_context(self) -> Context:
        """
        Responsável por retornar o contexto atual.
        Retorno:
            - O Contexto atual
        """
        objects: list[Object] = self._state.get_objects()
        
        factory = ContextFactory()
        return factory.create(objects)
