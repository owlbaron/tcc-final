"""TODO"""
from vision.contexts.context import Context

class FightMainMenuContext(Context):
    """TODO"""
    def get_valid_tokens(self) -> list[str]:
        """TODO"""
        default_tokens = self.super.get_valid_tokens()
        return default_tokens.append(["opção 1", "opção 2", "opção 3", "opção 4"])

    def get_commands(self, token: str) -> list[str]:
        """TODO"""
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
        """TODO"""
        # se tiver entre tal e tal só confirma se nao calcula se tem que subir ou descer
        return ["enter"]

    def _select_pokemon(self) -> list[str]:
        """TODO"""
        # se tiver entre tal e tal só confirma se nao calcula se tem que subir ou descer
        return ["right", "enter"]

    def _select_item(self) -> list[str]:
        """TODO"""
        # se tiver entre tal e tal só confirma se nao calcula se tem que subir ou descer
        return ["down", "enter"]

    def _select_run(self) -> list[str]:
        """TODO"""
        # se tiver entre tal e tal só confirma se nao calcula se tem que subir ou descer
        return ["down", "right", "enter"]
