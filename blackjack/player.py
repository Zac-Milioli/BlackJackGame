"""
## Player

Este módulo define a classe `Player` e suas funções
"""
from .card import Card
from .hand import Hand

class Player:
    """
    ## Jogador

    Contém os seguintes atributos:
    ```
    name: str
    hand: Hand
    ```
    """
    def __init__(self, name: str, hand: Hand = None, bank: int = 100,
                    wins: int = 0, losses: int = 0, card_counter: int = 0,
                    draws: int = 0, bet_counter: int = 0, blackjacks: int = 0):
        self._name: str = name
        self._hand: Hand = hand
        self._bank: int = bank
        self._wins: int = wins
        self._losses: int = losses
        self._draws: int = draws
        self._card_counter: int = card_counter
        self._bet_counter: int = bet_counter
        self._blackjacks: int = blackjacks

    @property
    def get_cards_string(self) -> list[str]:
        """
        Retorna as cartas que o jogador possui em formato str
        """
        return self._hand.get_cards_string

    @property
    def get_cards(self) -> list[Card]:
        """
        Retorna as cartas que o jogador possui
        """
        return self._hand.get_cards

    @property
    def get_name(self) -> str:
        """
        Retorna o nome do jogador
        """
        return self._name

    @property
    def get_bank(self) -> int:
        """
        Retorna quanto o jogador ainda possui para apostar
        """
        return self._bank

    @property
    def get_bet(self) -> int:
        """
        Retorna quanto o jogador ainda possui para apostar
        """
        return self._hand.get_bet

    @property
    def get_wins(self) -> int:
        """
        Retorna quantas rodadas o jogador ganhou
        """
        return self._wins

    @property
    def get_losses(self) -> int:
        """
        Retorna quantas rodadas o jogador perdeu
        """
        return self._losses

    @property
    def get_draws(self) -> int:
        """
        Retorna quantas rodadas o jogador empatou
        """
        return self._draws

    @property
    def get_card_counter(self) -> int:
        """
        Retorna quantas cartas o jogador já retirou no jogo
        """
        return self._card_counter

    @property
    def show_cards(self) -> str:
        """
        Exibe uma lista em formato de str com as cartas do jogador
        """
        return "\n\t- "+"\n\t- ".join(self._hand.get_cards_string)

    @property
    def get_sum(self) -> int:
        """
        Retorna a soma dos valores das cartas na mão
        """
        return self._hand.get_sum

    @property
    def get_bet_counter(self) -> int:
        """
        Retorna a soma dos valores das apostas
        """
        return self._bet_counter

    @property
    def get_blackjacks(self) -> int:
        """
        Retorna a quantidade de vezes que o jogador obteve 21
        """
        return self._blackjacks

    @property
    def description(self) -> str:
        """
        Retorna a descrição completa da situação de um jogador
        """
        part1 = f'{self._name}:\n\tSaldo: {self.get_bank}\n'
        part2 = f'\tAposta atual: {self.get_bet}\n\n\tSoma das cartas: {self.get_sum}'
        part3 = f'\n\tCartas:{self.show_cards}'
        return part1+part2+part3

    def add_blackjack(self):
        """
        Adiciona ao contador de vezes que o jogador obteve 21
        """
        self._blackjacks += 1

    def dealer_print(self, play_state: bool = False) -> str:
        """"
        Propriedade especial que retorna a string própria para o dealer
        """
        text = f'{self.get_name} possui {len(self.get_cards)} cartas'
        dealer_data = f"\nSaldo: {self.get_bank}\nAposta: {self.get_bet}"
        cards_sum = f' que somam {self.get_sum}'
        if not play_state:
            return text + dealer_data + f"\n\tCarta visível:\n\t- {self.get_cards_string[-1]}"
        return text + cards_sum + dealer_data + f"\n\tCartas:{self.show_cards}"

    def _add_bank(self, gains: int) -> None:
        """
        Acresce ao banco do jogador o valor indicado
        """
        self._bank += gains

    def _rm_bank(self, losses: int) -> None:
        """
        Remove do banco do jogador o valor indicado
        """
        self._bank -= losses

    def place_bet(self, bet: int) -> None:
        """
        Faz uma aposta
        """
        self._hand.set_bet(bet)
        self._rm_bank(bet)
        self._bet_counter += bet

    def win_round(self) -> None:
        """
        Ganha uma rodada
        """
        self._add_bank(self.get_bet*2)
        self._hand.set_bet(0)
        self._wins += 1

    def lose_round(self) -> None:
        """
        Perde uma rodada
        """
        self._hand.set_bet(0)
        self._losses += 1

    def draw(self) -> None:
        """
        Empata uma rodada
        """
        self._add_bank(self._hand.get_bet)
        self._hand.set_bet(0)
        self._draws += 1

    def add_card(self, new_cards: Card) -> None:
        """
        Adiciona uma carta no final do baralho do jogador
        """
        self._hand.add_card(new_cards)
        self._card_counter += 1

    def clear_cards(self) -> None:
        """
        Remove a primeira carta do baralho do usuário
        """
        self._hand.clear()

    def ace_save(self) -> bool:
        """
        Verifica se há Ace na mão do jogador, convertendo seu valor
        """
        return self._hand.ace_convert()

    def __str__(self) -> str:
        return f'{self._name} possui {len(self._hand)} cartas que somam {self.get_sum}'
