from vision.object import Object
from vision.state import State


class StateWriter:
    """
    Classe que será responsável por escrever no estado.
    O objetivo com isso é que fique bem fácil de depurar e manter o código,
    além de sabermos quem está escrevendo/lendo do estado.
    """
    _state: State

    def __init__(self) -> None:
        self._state = State()

    def write_result(self, result: list[tuple[int, str, tuple[int,int,int,int]]]) -> None:
        """
        Responsável por carregar o resultado do modelo no estado.
        Parâmetros:
            - result: Array de objetos reconhecidos: [(class_id, class_name, (box))]
        """
        self._state.clear()

        for item in result:
            class_id, class_name, box = item
            self._state.add_object(object=Object(class_id, class_name, box))
