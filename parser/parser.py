from lexer.lexer import Lexer, Token, TokenId
from typing import Union


class Parser:
    """Classe"""
    def __init__(self, lexer: Lexer) -> None:
        self._lexer = lexer

    def parse(self) -> Union[str, None]:
        return self._phrase()

    def _phrase(self) -> Union[str, None]:
        # token = self._lexer.next()

        # if token.getId() == TokenId.SUBJECT:
        #     return self._verb()
        # elif token.getId() == TokenId.IMPERATIVE or token.getId() == TokenId.INFINITIVE:
        #     pass
        # else:
        #     return None
        token = self._lexer.next()
        result: Union[str, None] = None

        if token.getId() == TokenId.SUBJECT:
            result = self._subject()
        elif token.getId() == TokenId.IMPERATIVE:
            result = self._imperative()
        elif token.getId() == TokenId.INFINITIVE:
            result = self._infinitive()
        elif token.getId() == TokenId.DIRECTION:
            result = self._direction()
        elif token.getId() == TokenId.ORDINAL:
            result = self._ordinal()

        return result

        # subject = self._subject()

        # if token.getId() == TokenId.IMPERATIVE:
        #     self._verb()
        #     self._imperative_verb_preposition()
        # elif token.getId() == TokenId.INFINITIVE:
        #     self._verb()
        # else:
        #     return None



    def _subject(self) -> Union[Token, None]:
        token = self._lexer.next()
        result: Union[str, None] = None

        if token.getId() == TokenId.INFINITIVE:
            result = self._infinitive()
        elif token.getId() == TokenId.IMPERATIVE:
            result = self._imperative()

        return result

    def _preposition(self) -> Union[str, None]:
        token = self._lexer.next()
        result: Union[str, None] = None

        if token.getId() == TokenId.DIRECTION:
            result = self._direction()
        elif token.getId() == TokenId.ORDINAL:
            result = self._ordinal()
        elif token.getId() == TokenId.INFINITIVE:
            result = self._infinitive()
        elif token.getValue() == "mochila":
            result = token

        return result

    def _definite_article(self)-> Union[str, None]:
        token = self._lexer.next()
        result: Union[str, None] = None

        if token.getId() == TokenId.ORDINAL:
            result = self._ordinal()

        return result

    def _ordinal(self)-> Union[str, None]:
        token = self._lexer.next()
        result: Union[str, None] = None

        if token.getId() == TokenId.SUBSTANTIVE:
            result = self._substantive()

        return result

    def _imperative(self) -> Union[Token, None]:
        token = self._lexer.next()
        result: Union[str, None] = None

        if token.getId() == TokenId.PREPOSITION:
            result = self._preposition()
        elif token.getId() == TokenId.DEFINITE_ARTICLE:
            result = self._definite_article()

        return result

    def _infinitive(self) -> Union[str, None]:
        token = self._lexer.peek()
        result: Union[str, None] = None

        if token.getId() == TokenId.PREPOSITION:
            result = self._preposition()
        elif token.getId() == TokenId.DEFINITE_ARTICLE:
            result = self._definite_article()
        else:
            result = self._lexer.next()

        return result

    def _direction(self) -> Union[str, None]:
        return self._lexer.next()

    def _substantive(self) -> Union[str, None]:
        return self._lexer.next()
