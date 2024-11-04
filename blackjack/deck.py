"""
## Deck

Este módulo define a classe `Deck` e suas funções
"""
from random import shuffle
from .card_vars import BlackJackVars
from .card import Card

class Deck:
    """
    ## Baralho de cartas.

    Contém os seguintes atributos:
    ```
    cards: list
    ```
    """
    def __init__(self):
        self._cards: list = []
        for suit in BlackJackVars.SUITS:
            for rank in BlackJackVars.RANKS:
                self._cards.append(Card(suit=suit, rank=rank))

    @property
    def get_cards(self) -> list:
        """
        Retorna a lista de cartas do baralho, em formato de string
        ```
        self.value
        ```
        """
        cards_list = []
        for card in self._cards:
            cards_list.append(f"{card}")
        return cards_list

    def shuffle_deck(self) -> None:
        """
        Embaralha as cartas do baralho.
        """
        shuffle(self._cards)

    def deal_one(self) -> Card:
        """
        Entrega a última carta do Deck para o jogador
        """
        return self._cards.pop()

    def __str__(self) -> str:
        return f"Deck of cards with: {', '.join(self.get_cards)}"

    def __len__(self) -> int:
        return len(self.get_cards)
