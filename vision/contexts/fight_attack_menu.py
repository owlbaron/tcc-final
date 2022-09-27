"""Classe FightAttackMenuContext"""
from vision.contexts.context import Context

class FightAttackMenuContext(Context):
    """
    Contexto que se encontra o jogo no momento.

    Em batalha escolhendo entre os ataques disponíveis.
    """

    def __str__(self):
        return f"Contexto de seleção de ataque (FightAttackMenuContext), opçoẽs validas: {self.get_valid_tokens()}"

    def get_valid_tokens(self) -> list[str]:
        """
        Retorna os tokens possíveis para esse estado que são os quatro ataques,
        além de sempre possibilitar os comandos padrões do emulador.
        """
        default_tokens = super().get_valid_tokens()
        return default_tokens + ["opção 1", "opção 2", "opção 3", "opção 4"]

    def get_commands(self, token: str) -> list[str]:
        """
        Retorna a os comandos a serem executados de acordo com o token passado, 
        dado o contexto atual.
        """
        d = {
            "opção 1": self._select_attack_one,
            "opção 2": self._select_attack_two,
            "opção 3": self._select_attack_three,
            "opção 4": self._select_attack_four,
        }

        if token in d:
            fn = d[token]

            return fn()
        else:
            return super().get_commands(token)

    # valida
    # handle
    # 

    def _select_attack_one(self) -> list[str]:
        """
        Seleciona o primeiro ataque. 

        Acha onde está o indicador e realiza os cálculos para selecionar o primeiro ataque.

        Retorno:
            - Lista de tokens de comando para selecionar o primeiro ataque.
        """

        # TODO se tiver entre tal e tal só confirma se nao calcula se tem que subir ou descer
        return ["x"]

    def _select_attack_two(self) -> list[str]:
        """
        Seleciona o segundo ataque. 

        Acha onde está o indicador e realiza os cálculos para selecionar o segundo ataque.

        Retorno:
            - Lista de tokens de comando para selecionar o segundo ataque.
        """

        # TODO se tiver entre tal e tal só confirma se nao calcula se tem que subir ou descer
        return ["down", "x"]

    def _select_attack_three(self) -> list[str]:
        """
        Seleciona o terceiro ataque. 

        Acha onde está o indicador e realiza os cálculos para selecionar o terceiro ataque.

        Retorno:
            - Lista de tokens de comando para selecionar o terceiro ataque.
        """
        
        # TODO se tiver entre tal e tal só confirma se nao calcula se tem que subir ou descer
        return ["down", "down", "x"]

    def _select_attack_four(self) -> list[str]:
        """
        Seleciona o quarto ataque. 

        Acha onde está o indicador e realiza os cálculos para selecionar o quarto ataque.

        Retorno:
            - Lista de tokens de comando para selecionar o quarto ataque.
        """
        
        # TODO se tiver entre tal e tal só confirma se nao calcula se tem que subir ou descer
        return ["down", "down", "down", "x"]
