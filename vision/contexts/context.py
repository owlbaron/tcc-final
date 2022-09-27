"""Classe de contexto do emulador"""
class Context:
    """
    Contexto que se encontra o jogo no momento.

    Exemplo:
        - FightMainMenu: Em batalha escolhendo entre atacar, pokemon, bag ou run.
        - FightAttackMenu: Em batalha escolhendo entre os ataques disponíveis.
        - YesNoMenu: Escolhendo entre sim ou não.
    """

    def __str__(self):
        return f"Contexto generico (Context), opçoẽs validas: {self.get_valid_tokens()}"

    def get_valid_tokens(self) -> list[str]:
        """
        Retorna o conjunto de opções válidas para determinado contexto.
        Na classe "Context" tem a lista de opções válidas por padrão, 
        como os comandos do emulador.
        """
        return ["cima", "baixo", "esquerda", "direita", "seleciona", "a", "cancela", "b"]

    def get_commands(self, token: str) -> list[str]:
        """
        Retorna a os comandos a serem executados de acordo com o token passado, 
        dado o contexto atual.
        """
        d = {
            "cima": self._go_up,
            "baixo": self._go_down,
            "esquerda": self._go_left,
            "direita": self._go_right,
            "seleciona": self._select,
            "a": self._select,
            "cancela" : self._cancel,
            "b" : self._cancel,
        }

        fn = d[token]

        return fn()

    def _go_up(self) -> list[str]:
        """Retorna o token de comando para cima"""
        return ["up"]

    def _go_down(self) -> list[str]:
        """Retorna o token de comando para baixo"""
        return ["down"]

    def _go_left(self) -> list[str]:
        """Retorna o token de comando para esquerda"""
        return ["left"]

    def _go_right(self) -> list[str]:
        """Retorna o token de comando para direita"""
        return ["right"]

    def _select(self) -> list[str]:
        """Retorna o token de comando para selecionar/confirmar"""
        return ["x"]

    def _cancel(self) -> list[str]:
        """Retorna o token de comando para cancelar/voltar"""
        return ["z"]
