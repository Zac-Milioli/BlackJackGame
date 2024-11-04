"""
Testes para o módulo Player
"""

from blackjack import Player, Card, Hand

class TestPlayer:
    """
    Classe para uso do Pytest
    """
    test_card = Card(suit="Test", rank="Ace")

    def test_01_create_player(self):
        """
        Testa a criação de um Player
        """
        test_hand = Hand()
        test_player = Player(name="TestPlayer", hand=test_hand)
        assert not test_player.get_cards_string
        assert test_player.get_name == "TestPlayer"

    def test_02_add_card(self):
        """
        Testa a adição de uma carta ao baralho do Player
        """
        test_hand = Hand()
        test_player = Player(name="TestPlayer", hand=test_hand)
        test_player.add_card(new_cards=self.test_card)
        assert len(test_player.get_cards_string) == 1

    def test_03_clear_hand(self):
        """
        Testa a remoção de cartas do baralho do Player
        """
        test_hand = Hand()
        test_player = Player(name="TestPlayer", hand=test_hand)
        test_player.add_card(new_cards=self.test_card)
        test_player.clear_cards()
        assert len(test_player.get_cards) == 0

    def test_04_convert_ace(self):
        """
        Testa a conversão do Ace
        """
        test_hand = Hand()
        test_player = Player(name="TestPlayer", hand=test_hand)
        test_player.add_card(new_cards=self.test_card)
        test_hand.ace_convert()
        assert test_player.get_cards[0].get_value == 1

    def test_05_place_bet(self):
        """
        Testa a função de ganhar um round
        """
        test_hand = Hand()
        test_player = Player(name="TestPlayer", hand=test_hand, bank=100)
        assert test_player.get_bet == 0
        test_player.place_bet(10)
        assert test_player.get_bet == 10
        assert test_player.get_bank == 90

    def test_06_win_round(self):
        """
        Testa a função de ganhar um round
        """
        test_hand = Hand()
        test_player = Player(name="TestPlayer", hand=test_hand, bank=100)
        test_player.place_bet(10)
        test_player.win_round()
        assert test_player.get_bet == 0
        assert test_player.get_bank == 110
        assert test_player.get_wins == 1
    
    def test_07_lose_round(self):
        """
        Testa a função de ganhar um round
        """
        test_hand = Hand()
        test_player = Player(name="TestPlayer", hand=test_hand, bank=100)
        test_player.place_bet(10)
        test_player.lose_round()
        assert test_player.get_bet == 0
        assert test_player.get_bank == 90
        assert test_player.get_losses == 1
