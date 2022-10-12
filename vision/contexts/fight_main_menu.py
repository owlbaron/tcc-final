"""Classe FightMainMenuContext"""
from constants.commands import EmulatorCommand
from vision.contexts.context import Context
from vision.object import Object

class FightMainMenuContext(Context):
    """
    Contexto que se encontra o jogo no momento.

    Em batalha escolhendo entre atacar, pokemon, bag ou run.
    """
    _indicator: Object | None = None

    def __init__(self, indicator: Object | None) -> None:
        super().__init__()
        self._indicator = indicator

    def __str__(self):
        return f"Contexto de menu da batalha (FightMainMenuContext), opçoẽs validas: {self.get_valid_tokens()}"

    def get_valid_tokens(self) -> list[str]:
        """
        Retorna os tokens possíveis para esse estado que são as quatro 
        opções attack, pkmn, bag e run, além de sempre possibilitar 
        os comandos padrões do emulador.
        """
        default_tokens = super().get_valid_tokens()
        return default_tokens + ["opção 1", "opção 2", "opção 3", "opção 4", "lutar", "batalhar", "pokemon", "pokémon", "item" , "itens", "fugir", "correr"]

    def get_commands(self, token: str) -> list[EmulatorCommand]:
        """
        Retorna a os comandos a serem executados de acordo com o token passado, 
        dado o contexto atual.
        """
        d = {
            "opção 1": self._select_fight,
            "opção 2": self._select_pokemon,
            "opção 3": self._select_item,
            "opção 4": self._select_run,
            "lutar": self._select_fight,
            "batalhar": self._select_fight,
            "pokemon": self._select_pokemon,
            "pokémon": self._select_pokemon,
            "item": self._select_item,
            "itens": self._select_item,
            "fugir": self._select_run,
            "correr": self._select_run
        }

        if token in d:
            fn = d[token]

            return fn()
        else:
            return super().get_commands(token)

    def _find_command_path(self, x: float, y: float) -> list[EmulatorCommand]:
        box_indicator = self._indicator.get_box()
        xi, yi = box_indicator[0:2]
        commands = []

        if x - xi > 0.02:
            commands.append(EmulatorCommand.RIGHT)
        elif x - xi < -0.02:
            commands.append(EmulatorCommand.LEFT)

        if y - yi > 0.02:
            commands.append(EmulatorCommand.DOWN)
        elif y - yi < -0.02:
            commands.append(EmulatorCommand.UP)
        

        commands.append(EmulatorCommand.A)

        return commands


    def _select_fight(self) -> list[EmulatorCommand]:
        """
        Seleciona a opção de ataque

        Acha onde está o indicador e realiza os cálculos para selecionar a opção de ataque.

        Retorno:
            - Lista de tokens de comando para selecionar o primeiro ataque.
        """

        # Magic Numbers (posição do fight) 
        x, y = [0.4719102, 0.81814855]

        if self._indicator == None:
            return [EmulatorCommand.LEFT, EmulatorCommand.UP, EmulatorCommand.A]
        
        return self._find_command_path(x, y)
        
    def _select_pokemon(self) -> list[EmulatorCommand]:
        """
        Seleciona a opção de escolher pokemon

        Acha onde está o indicador e realiza os cálculos para selecionar a opção de escolher pokemon.

        Retorno:
            - Lista de tokens de comando para selecionar a opção de escolher pokemon.
        """

        # Magic Numbers
        x, y = [0.7725144, 0.8188903]

        if self._indicator == None:
            return [EmulatorCommand.RIGHT, EmulatorCommand.UP, EmulatorCommand.A]

        return self._find_command_path(x, y)

    def _select_item(self) -> list[EmulatorCommand]:
        """
        Seleciona a opção de escolher item (bag)

        Acha onde está o indicador e realiza os cálculos para selecionar a opção de escolher item (bag).

        Retorno:
            - Lista de tokens de comando para selecionar a opção de escolher item (bag).
        """

        # Magic Numbers
        x, y = [0.4694635, 0.91984713]

        if self._indicator == None:
            return [EmulatorCommand.LEFT, EmulatorCommand.DOWN, EmulatorCommand.A]

        return self._find_command_path(x, y)

    def _select_run(self) -> list[EmulatorCommand]:
        """
        Seleciona a opção de fugir

        Acha onde está o indicador e realiza os cálculos para selecionar a opção de fugir.

        Retorno:
            - Lista de tokens de comando para selecionar a opção de fugir.
        """
        
        # Magic Numbers
        x, y = [0.77355987, 0.92586845]

        if self._indicator == None:
            return [EmulatorCommand.DOWN, EmulatorCommand.RIGHT, EmulatorCommand.A]

        return self._find_command_path(x, y)
