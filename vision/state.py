from metaclass.singleton import SingletonMeta
from vision.object import Object

class State(metaclass=SingletonMeta):
    _objects: list[Object] = []

    def clear(self) -> None:
        """Responsável por limpar o estado."""
        self._objects = []

    def add_object(self, obj: Object) -> None:
        """
        Responsável por adicionar um objeto no estado.
        Parâmetros:
            - object: Um objeto que está sendo detectado pelo modelo.
        """
        self._objects.append(obj)

    def get_objects(self) -> list[Object]:
        """
        Disponibiliza os objetos que estão em tela.
        Retorno:
            - list[object]: Objetos que estão sendo detectados pelo modelo.
        """
        return self._objects
