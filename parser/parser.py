from lexer.lexer import Lexer, TokenId


class Parser:
    """Classe"""
    def __init__(self, lexer: Lexer) -> None:
        self._lexer = lexer

    def parse(self) -> str | None:
        return self.phrase()

    def phrase(self) -> str | None:
        token = self._lexer.next()

        if token.getId() == TokenId.SUBJECT:
            pass
        elif token.getId() == TokenId.IMPERATIVE:
            pass
        elif token.getId() == TokenId.INFINITIVE:
            pass
        elif token.getId() == TokenId.DIRECTION:
            pass
        else:
            return None
    
