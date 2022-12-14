"""Classe YesNoMenuContext"""
from vision.contexts.context import Context
from vision.object import Object
from constants.commands import EmulatorCommand

class YesNoMenuContext(Context):
    """
    Contexto que se encontra o jogo no momento.

    Escolhendo entre sim ou não.
    """
    def __init__(self, indicator: Object | None) -> None:
        super().__init__()
        self._indicator = indicator

    def __str__(self):
        return f"Contexto de seleção de sim ou não (YesNoMenuContext), opçoẽs validas: {self.get_valid_tokens()}"

    def get_valid_tokens(self) -> list[str]:
        """
        Retorna os tokens possíveis para esse estado que são sim e não,
        além de sempre possibilitar os comandos padrões do emulador.
        """
        default_tokens = super().get_valid_tokens()
        return default_tokens + ["sim", "não", "opção 1", "opção 2"]

    def get_commands(self, token: str) -> list[EmulatorCommand]:
        """
        Retorna a os comandos a serem executados de acordo com o token passado, 
        dado o contexto atual.
        """
        d = {
            "opção 1": self._select_yes_option,
            "sim": self._select_yes_option,
            "opção 2": self._select_no_option,
            "não": self._select_no_option,
        }

        if token in d:
            fn = d[token]

            return fn()
        else:
            return super().get_commands(token)

    # valida
    # handle
    # 

    def _select_yes_option(self) -> list[EmulatorCommand]:
        """
        Seleciona o sim

        Acha onde está o indicador e realiza os cálculos para selecionar a opção sim.

        Retorno:
            - Lista de tokens de comando para selecionar o sim.
        """

        # TODO se tiver entre tal e tal só confirma se nao calcula se tem que subir ou descer
        return [EmulatorCommand.A]

    def _select_no_option(self) -> list[EmulatorCommand]:
        """
        Seleciona o não

        Acha onde está o indicador e realiza os cálculos para selecionar a opção não.

        Retorno:
            - Lista de tokens de comando para selecionar o não.
        """

        # TODO se tiver entre tal e tal só confirma se nao calcula se tem que subir ou descer
        return [EmulatorCommand.DOWN, EmulatorCommand.A]