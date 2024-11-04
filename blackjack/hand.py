"""
## Hand

Este módulo define a classe `Hand` e suas funções
"""
from .card import Card

class Hand:
    """
    ## Mão do jogador.

    Contém os seguintes atributos:
    ```
    cards: list
    sum_cards: int
    ```
    """
    def __init__(self, bet: int = 0):
        self._cards: list = []
        self._sum_cards: int = 0
        self._bet: int = bet

    @property
    def get_cards_string(self) -> list[str]:
        """
        Retorna a lista de cartas da mão, em formato de string
        """
        cards_list = []
        for card in self._cards:
            cards_list.append(f"{card}")
        return cards_list

    @property
    def get_cards(self) -> list[Card]:
        """
        Retorna a lista de cartas da mão
        """
        return self._cards

    @property
    def get_sum(self) -> int:
        """
        Retorna a soma dos valores das cartas na mão
        """
        return self._sum_cards

    @property
    def get_bet(self) -> int:
        """
        Retorna o valor da aposta atual
        """
        return self._bet

    def set_bet(self, new_bet: int) -> None:
        """
        Altera o valor da aposta atual
        """
        self._bet = new_bet

    def order_cards(self) -> None:
        """
        Ordena as cartas por valor em ordem crescente
        """
        self._cards.sort()

    def add_card(self, new_card: Card) -> None:
        """
        Adiciona uma carta na mão do jogador
        """
        self._cards.append(new_card)
        self.order_cards()
        self._sum_cards += new_card.get_value

    def clear(self) -> None:
        """
        Remove todas as cartas da mão do jogador
        """
        self._cards = []
        self._sum_cards = 0

    def ace_convert(self) -> bool:
        """
        Altera o valor do Ace para 1 (considerando que o Ace sempre será o último da lista)
        """
        card = self._cards.pop()
        if "Ace" in card.get_rank:
            card.set_value(1)
            self.add_card(card)
            self._sum_cards -= 10
            return True
        self._cards.append(card)
        return False

    def __len__(self):
        return len(self._cards)
