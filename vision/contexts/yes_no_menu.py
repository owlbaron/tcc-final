"""Classe YesNoMenuContext"""
from vision.contexts.context import Context

class YesNoMenuContext(Context):
    """
    Contexto que se encontra o jogo no momento.

    Escolhendo entre sim ou não.
    """
    def get_valid_tokens(self) -> list[str]:
        """
        Retorna os tokens possíveis para esse estado que são os quatro ataques,
        além de sempre possibilitar os comandos padrões do emulador.
        """
        default_tokens = self.super.get_valid_tokens()
        return default_tokens.append(["sim", "não", "opção 1", "opção 2"])

    def get_commands(self, token: str) -> list[str]:
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

        fn = d[token]

        return fn()

    # valida
    # handle
    # 

    def _select_yes_option(self) -> list[str]:
        """
        Seleciona o sim

        Acha onde está o indicador e realiza os cálculos para selecionar a opção sim.

        Retorno:
            - Lista de tokens de comando para selecionar o sim.
        """

        # TODO se tiver entre tal e tal só confirma se nao calcula se tem que subir ou descer
        return ["enter"]

    def _select_no_option(self) -> list[str]:
        """
        Seleciona o não

        Acha onde está o indicador e realiza os cálculos para selecionar a opção não.

        Retorno:
            - Lista de tokens de comando para selecionar o não.
        """

        # TODO se tiver entre tal e tal só confirma se nao calcula se tem que subir ou descer
        return ["down", "enter"]