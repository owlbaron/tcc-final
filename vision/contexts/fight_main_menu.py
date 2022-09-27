"""Classe FightMainMenuContext"""
from vision.contexts.context import Context

class FightMainMenuContext(Context):
    """
    Contexto que se encontra o jogo no momento.

    Em batalha escolhendo entre atacar, pokemon, bag ou run.
    """

    def get_valid_tokens(self) -> list[str]:
        """
        Retorna os tokens possíveis para esse estado que são os quatro ataques,
        além de sempre possibilitar os comandos padrões do emulador.
        """
        default_tokens = self.super.get_valid_tokens()
        return default_tokens.append(["opção 1", "opção 2", "opção 3", "opção 4"])

    def get_commands(self, token: str) -> list[str]:
        """
        Retorna a os comandos a serem executados de acordo com o token passado, 
        dado o contexto atual.
        """
        d = {
            "opção 1": self._select_fight,
            "opção 2": self._select_pokemon,
            "opção 3": self._select_item,
            "opção 4": self._select_run,
        }

        if token in d:
            fn = d[token]

            return fn()
        else:
            return self.super.get_commands(token)

    # valida
    # handle
    # 

    def _select_fight(self) -> list[str]:
        """
        Seleciona a opção de ataque

        Acha onde está o indicador e realiza os cálculos para selecionar a opção de ataque.

        Retorno:
            - Lista de tokens de comando para selecionar o primeiro ataque.
        """

        # TODO se tiver entre tal e tal só confirma se nao calcula se tem que subir ou descer
        return ["enter"]

    def _select_pokemon(self) -> list[str]:
        """
        Seleciona a opção de escolher pokemon

        Acha onde está o indicador e realiza os cálculos para selecionar a opção de escolher pokemon.

        Retorno:
            - Lista de tokens de comando para selecionar a opção de escolher pokemon.
        """

        # TODO se tiver entre tal e tal só confirma se nao calcula se tem que subir ou descer
        return ["right", "enter"]

    def _select_item(self) -> list[str]:
        """
        Seleciona a opção de escolher item (bag)

        Acha onde está o indicador e realiza os cálculos para selecionar a opção de escolher item (bag).

        Retorno:
            - Lista de tokens de comando para selecionar a opção de escolher item (bag).
        """

        # TODO se tiver entre tal e tal só confirma se nao calcula se tem que subir ou descer
        return ["down", "enter"]

    def _select_run(self) -> list[str]:
        """
        Seleciona a opção de fugir

        Acha onde está o indicador e realiza os cálculos para selecionar a opção de fugir.

        Retorno:
            - Lista de tokens de comando para selecionar a opção de fugir.
        """

        # TODO se tiver entre tal e tal só confirma se nao calcula se tem que subir ou descer
        return ["down", "right", "enter"]
