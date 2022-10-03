"""Classe de contexto do emulador"""
from constants.commands import EmulatorCommand


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
        return ["cima", "baixo", "esquerda", "direita", "seleciona", "a", "ok", "cancela", "b", "start"]

    def get_commands(self, token: str) -> list[EmulatorCommand]:
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
            "ok": self._select,
            "cancela" : self._cancel,
            "b" : self._cancel,
            "start": self._start
        }

        fn = d[token]

        return fn()

    def _go_up(self) -> list[EmulatorCommand]:
        """Retorna o token de comando para cima"""
        return [EmulatorCommand.UP]

    def _go_down(self) -> list[EmulatorCommand]:
        """Retorna o token de comando para baixo"""
        return [EmulatorCommand.DOWN]

    def _go_left(self) -> list[EmulatorCommand]:
        """Retorna o token de comando para esquerda"""
        return [EmulatorCommand.LEFT]

    def _go_right(self) -> list[EmulatorCommand]:
        """Retorna o token de comando para direita"""
        return [EmulatorCommand.RIGHT]

    def _select(self) -> list[EmulatorCommand]:
        """Retorna o token de comando para selecionar/confirmar"""
        return [EmulatorCommand.A]

    def _cancel(self) -> list[EmulatorCommand]:
        """Retorna o token de comando para cancelar/voltar"""
        return [EmulatorCommand.B]

    def _start(self) -> list[EmulatorCommand]:
        return [EmulatorCommand.START]