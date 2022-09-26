"""TODO"""
from vision.contexts.context import Context

class FightAttackMenuContext(Context):
    """TODO"""
    def get_valid_tokens(self) -> list[str]:
        """TODO"""
        default_tokens = self.super.get_valid_tokens()
        return default_tokens.append(["opção 1", "opção 2", "opção 3", "opção 4"])

    def get_commands(self, token: str) -> list[str]:
        """TODO"""
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
            return self.super.get_commands(token)

    # valida
    # handle
    # 

    def _select_attack_one(self) -> list[str]:
        """TODO"""
        # se tiver entre tal e tal só confirma se nao calcula se tem que subir ou descer
        return ["enter"]

    def _select_attack_two(self) -> list[str]:
        """TODO"""
        # se tiver entre tal e tal só confirma se nao calcula se tem que subir ou descer
        return ["down", "enter"]

    def _select_attack_three(self) -> list[str]:
        """TODO"""
        # se tiver entre tal e tal só confirma se nao calcula se tem que subir ou descer
        return ["down", "down", "enter"]

    def _select_attack_four(self) -> list[str]:
        """TODO"""
        # se tiver entre tal e tal só confirma se nao calcula se tem que subir ou descer
        return ["down", "down", "down", "enter"]
