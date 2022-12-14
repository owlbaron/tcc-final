"""
O módulo de vision será o local onde toda lógica referente a "visão"
do nosso programa ficará
"""

class Object:
    """Object nada mais é que um objeto que está sendo detectado pelo modelo"""
    _class_id: int
    _class_name: str
    _box: tuple[float,float,float,float]

    def __str__(self) -> str:
        return f"{self._class_name}({self._class_id})"
    
    def __repr__(self) -> str:
        return self.__str__()

    def __init__(self, class_id: int, class_name: str, box: tuple[float,float,float,float]) -> None:
        self._class_id = class_id
        self._class_name = class_name
        self._box = box

    def get_class_id(self) -> int:
        """Retorna o Class id"""
        return self._class_id
    
    def get_box(self) -> tuple[float,float,float,float]:
        """Retorna a posição + altura do objeto"""
        return self._box
