"""Classe FightAttackMenuContext"""
from math import ceil
from constants.commands import EmulatorCommand
from vision.contexts.context import Context
from vision.object import Object

class FightAttackMenuContext(Context):
    """
    Contexto que se encontra o jogo no momento.

    Em batalha escolhendo entre os ataques disponíveis.
    """
    def __init__(self, indicator: Object | None) -> None:
        super().__init__()
        self._indicator = indicator

    def __str__(self):
        return f"Contexto de seleção de ataque (FightAttackMenuContext), opçoẽs validas: {self.get_valid_tokens()}"

    def get_valid_tokens(self) -> list[str]:
        """
        Retorna os tokens possíveis para esse estado que são os quatro ataques,
        além de sempre possibilitar os comandos padrões do emulador.
        """
        default_tokens = super().get_valid_tokens()
        return default_tokens + ["opção 1", "opção 2", "opção 3", "opção 4"]

    def _find_command_path(self, y: float) -> list[EmulatorCommand]:
        box_indicator = self._indicator.get_box()
        yi = box_indicator[1]
        hi = box_indicator[3]
        commands = []

        if y - yi > 0.02:
            presses = ceil((y - yi) / hi)
            commands += [EmulatorCommand.DOWN] * presses
        elif y - yi < -0.02:
            presses = ceil(abs((y - yi)) / hi)
            commands += [EmulatorCommand.UP] * presses
        

        commands.append(EmulatorCommand.A)

        return commands

    def get_commands(self, token: str) -> list[EmulatorCommand]:
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

    def _select_attack_one(self) -> list[EmulatorCommand]:
        """
        Seleciona o primeiro ataque. 

        Acha onde está o indicador e realiza os cálculos para selecionar o primeiro ataque.

        Retorno:
            - Lista de tokens de comando para selecionar o primeiro ataque.
        """
        y = 0.7650474

        if self._indicator == None:
            return [EmulatorCommand.A]
            
        return self._find_command_path(y)

    def _select_attack_two(self) -> list[EmulatorCommand]:
        """
        Seleciona o segundo ataque. 

        Acha onde está o indicador e realiza os cálculos para selecionar o segundo ataque.

        Retorno:
            - Lista de tokens de comando para selecionar o segundo ataque.
        """
        y = 0.8185282

        if self._indicator == None:
            return [EmulatorCommand.DOWN, EmulatorCommand.A]
            
        return self._find_command_path(y)

    def _select_attack_three(self) -> list[EmulatorCommand]:
        """
        Seleciona o terceiro ataque. 

        Acha onde está o indicador e realiza os cálculos para selecionar o terceiro ataque.

        Retorno:
            - Lista de tokens de comando para selecionar o terceiro ataque.
        """
        y = 0.872

        if self._indicator == None:
            return [EmulatorCommand.DOWN, EmulatorCommand.DOWN, EmulatorCommand.A]
            
        return self._find_command_path(y)

    def _select_attack_four(self) -> list[EmulatorCommand]:
        """
        Seleciona o quarto ataque. 

        Acha onde está o indicador e realiza os cálculos para selecionar o quarto ataque.

        Retorno:
            - Lista de tokens de comando para selecionar o quarto ataque.
        """
        y = 0.9255
        
        if self._indicator == None:
            return [EmulatorCommand.DOWN, EmulatorCommand.DOWN, EmulatorCommand.DOWN, EmulatorCommand.A]
            
        return self._find_command_path(y)
