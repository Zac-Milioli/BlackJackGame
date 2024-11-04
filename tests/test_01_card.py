"""
Testes para o módulo Card
"""

from blackjack import Card, BlackJackVars

class TestCard:
    """
    Classe para uso do Pytest
    """
    def test_01_create_card(self):
        """
        Testa a criação de um Card
        """
        test_card = Card(suit=BlackJackVars.SUITS[0], rank=BlackJackVars.RANKS[0])
        assert test_card.get_suit == BlackJackVars.SUITS[0]
        assert test_card.get_rank == BlackJackVars.RANKS[0]
        assert test_card.get_value == BlackJackVars.VALUES[BlackJackVars.RANKS[0]]

    def test_02_create__high_value_card(self):
        """
        Testa a criação de um Card com valor mais alto 
        """
        test_card = Card(suit=BlackJackVars.SUITS[-1], rank=BlackJackVars.RANKS[-1])
        assert test_card.get_suit == BlackJackVars.SUITS[-1]
        assert test_card.get_rank == BlackJackVars.RANKS[-1]
        assert test_card.get_value == BlackJackVars.VALUES[BlackJackVars.RANKS[-1]]
