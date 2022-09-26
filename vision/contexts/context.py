"""TODO"""
class Context:
    """TODO"""
    def get_valid_tokens(self) -> list[str]:
        """TODO"""
        return ["cima", "baixo", "esquerda", "direita", "seleciona", "cancela"]

    def get_commands(self, token: str) -> None:
        """TODO"""
        d = {
            "cima": self._go_up,
            "baixo": self._go_down,
            "esquerda": self._go_left,
            "direita": self._go_right,
            "seleciona": self._select,
            "cancela" : self._cancel,
        }

        fn = d[token]

        return fn()

    def _go_up(self) -> list[str]:
        """TODO"""
        return ["up"]

    def _go_down(self) -> list[str]:
        """TODO"""
        return ["down"]

    def _go_left(self) -> list[str]:
        """TODO"""
        return ["left"]

    def _go_right(self) -> list[str]:
        """TODO"""
        return ["right"]

    def _select(self) -> list[str]:
        """TODO"""
        return ["a"]

    def _cancel(self) -> list[str]:
        """TODO"""
        return ["b"]
