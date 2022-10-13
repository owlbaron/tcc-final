from enum import Enum
from utils.load_json import load_json

class TokenId(Enum):
    PREPOSITION = "preposition"
    SUBSTANTIVE = "substantive"
    ORDINAL = "ordinal"
    INFINITIVE = "infinitive"
    IMPERATIVE = "imperative"
    SUBJECT = "subject"
    UNKNOWN = "unknown"

class Token:
    """."""
    def __init__(self, id: TokenId, value: str) -> None:
        self._id = id
        self._value = value
    
    def getId(self) -> TokenId:
        """"""
        return self._id
    
    def getValue(self) -> str:
        """"""
        return self._value


class Lexer:
    """."""
    def __init__(self, buffer: list[str]) -> None:
        self._buffer = buffer
        self._token_dict = load_json("input_token_dict.json")

    def peek(self) -> Token:
        return self._buffer[0]

    def next(self) -> Token:
        """."""
        first = self._buffer.pop(0)

        if first in self._token_dict.keys():
            token_id_str = self._token_dict[first]
            token_id = TokenId(token_id_str)
            return Token(token_id, first)

        return Token(TokenId.UNKNOWN, first)
