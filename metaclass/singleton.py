"""
Metaclass é um conceito de POO utilizado em python para criar classes cuja instâncias são classes.
Esse módulo é o responsável por armazenar as implementações de meta classes.
"""

class SingletonMeta(type):
    """
    O singleton é um design pattern que garante que apenas um objeto de um tipo
    existe e prove apenas um ponto de acesso para ele.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
