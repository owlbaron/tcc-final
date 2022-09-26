"""TODO"""
from vision.contexts.context import Context

class YesNoMenuContext(Context):
    """TODO"""
    def get_valid_tokens(self) -> list[str]:
        """TODO"""
        default_tokens = self.super.get_valid_tokens()
        return default_tokens.append(["sim", "não", "opção 1", "opção 2"])

    def get_commands(self, token: str) -> list[str]:
        """TODO"""
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
        """TODO"""
        # se tiver entre tal e tal só confirma se nao calcula se tem que subir ou descer
        return ["enter"]

    def _select_no_option(self) -> list[str]:
        """TODO"""
        # se tiver entre tal e tal só confirma se nao calcula se tem que subir ou descer
        return ["down", "enter"]