"""
## Card

Este módulo define a classe `Card` e suas funções
"""
from .card_vars import BlackJackVars

class Card:
    """
    ## Cartas do jogo.

    Contém os seguintes atributos:
    ```
    suit: str (Hearts, Diamonds, ...)

    rank: str (Two, Three, King, Ace, ...)

    value: int (Definido automaticamente)
    ```
    """
    def __init__(self, suit: str, rank: str):
        self._suit: str = suit
        self._rank: str = rank
        self._value: int = BlackJackVars.VALUES[self._rank]

    @property
    def get_suit(self) -> str:
        """
        Retorna o parâmetro suit em formato de string
        ```
        self.suit
        ```
        """
        return self._suit

    @property
    def get_rank(self) -> str:
        """
        Retorna o parâmetro rank em formato de string
        ```
        self.rank
        ```
        """
        return self._rank

    @property
    def get_value(self) -> int:
        """
        Retorna o parâmetro value em formato de int
        ```
        self.value
        ```
        """
        return self._value

    def set_value(self, value) -> None:
        """
        Modifica o valor de uma carta
        """
        self._value = value

    def __str__(self) -> str:
        return f'{self.get_rank} of {self.get_suit} ({self.get_value})'

    def __lt__(self, card_2) -> bool:
        return self.get_value < card_2.get_value

    def __gt__(self, card_2) -> bool:
        return self.get_value < card_2.get_value

    def __eq__(self, card_2) -> bool:
        return self.get_value == card_2.get_value
