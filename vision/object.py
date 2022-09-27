"""
O módulo de vision será o local onde toda lógica referente a "visão"
do nosso programa ficará
"""

class Object:
    """Object nada mais é que um objeto que está sendo detectado pelo modelo"""
    _class_id: int
    _class_name: str
    _box: tuple[int,int,int,int]

    def __init__(self, class_id: int, class_name: str, box: tuple[int,int,int,int]) -> None:
        self._class_id = class_id
        self._class_name = class_name
        self._box = box

    def get_class_id(self) -> int:
        """Retorna o Class id"""
        return self._class_id
