"""
Testes para o módulo Deck
"""

from blackjack import Deck, BlackJackVars

class TestDeck:
    """
    Classe para uso do Pytest
    """

    def test_01_create_deck(self):
        """
        Testa a criação de um Deck
        """
        test_deck = Deck()
        assert len(test_deck.get_cards) == 52
        assert test_deck.get_cards[0] == f'{BlackJackVars.RANKS[0]} of {BlackJackVars.SUITS[0]} ({BlackJackVars.VALUES.get(BlackJackVars.RANKS[0])})'

    def test_02_shuffle_deck(self):
        """
        Testa a função de embaralhar do Deck 
        """
        test_deck = Deck()
        deck_before = test_deck.get_cards
        test_deck.shuffle_deck()
        assert test_deck.get_cards != deck_before

    def test_03_deal_card(self):
        """
        Testa a função de distribuir cartas do Deck 
        """
        test_deck = Deck()
        first_card_expected = test_deck.get_cards[-1]
        second_card_expected = test_deck.get_cards[-2]
        first_card = test_deck.deal_one()
        second_card = test_deck.deal_one()
        assert str(first_card) == first_card_expected
        assert str(second_card) == second_card_expected
        assert len(test_deck.get_cards) == 50
