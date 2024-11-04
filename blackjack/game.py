"""
## Game

Este módulo permite instanciar um jogo e executá-lo
"""
from os import system as sys
from .player import Player
from .deck import Deck
from .hand import Hand

class Game:
    """
    Classe onde ocorre o jogo
    """
    def __init__(self, player_1: str, player_1_bank: int = 100, player_2: str = 'Dealer',
                    player_2_bank: int = 100, multiplayer: bool = False):
        self.player_1 = player_1
        self.player_1_bank = player_1_bank
        self.player_2 = player_2
        self.player_2_bank = player_2_bank
        self.multiplayer = multiplayer

    def run(self):
        """
        Função principal para iniciar o jogo
        """
        player_hand = Hand()
        player_1 = Player(name=self.player_1, hand=player_hand, bank=self.player_1_bank)
        player_2_hand = Hand()
        player_2 = Player(name=self.player_2, hand=player_2_hand, bank=self.player_2_bank)

        playing = True
        winner = None
        last_round = ""
        turn = 1
        while playing:
            sys("cls")
            player_1.clear_cards()
            player_2.clear_cards()

            deck = Deck()
            deck.shuffle_deck()
            player_1.add_card(deck.deal_one())
            player_1.add_card(deck.deal_one())
            player_2.add_card(deck.deal_one())
            player_2.add_card(deck.deal_one())

            print(last_round)
            print(f"Rodada {turn}")
            print('- '*30)
            if self.multiplayer:
                print(player_2.description)
            else:
                print(player_2.dealer_print())
            print('- '*30)
            print(player_1.description)
            print('- '*30)

            if player_1.get_bank <= 0:
                playing = False
                winner = player_2
                break
            if player_2.get_bank <= 0:
                playing = False
                winner = player_1
                break

            betting = True
            max_val = min([player_1.get_bank, player_2.get_bank])
            while betting:
                print(f"\nAposta máxima possível: {max_val}\n\nInsira um valor para apostar")
                bet = input('...')
                if bet.isdigit():
                    value = int(bet)
                    if value <= max_val:
                        player_1.place_bet(value)
                        player_2.place_bet(value)
                        betting = False
                        break
                print("\nValor inválido\n")

            round_over = False
            while not round_over:

                player_1_turn = True
                while player_1_turn:

                    if player_1.get_sum > 21:
                        if not player_1.ace_save():
                            round_over = True
                            player_2.win_round()
                            player_1.lose_round()
                            player_1_turn = False
                            sys("cls")
                            print(f"Rodada {turn}")
                            print('- '*30)
                            print(player_2)
                            print('- '*30)
                            print(player_1.description)
                            print('- '*30)
                            last_round = f"\nVencedor da última rodada: {player_2.get_name}\n"
                            print(f"\n\nVencedor: {player_2.get_name}")
                            input('\n[ENTER] Prosseguir...\n')
                            break
                    if player_1.get_sum == 21:
                        player_1.add_blackjack()

                    sys("cls")
                    print(f"Rodada {turn}")
                    print('- '*30)
                    if self.multiplayer:
                        print(player_2)
                    else:
                        print(player_2.dealer_print())
                    print('- '*30)
                    print(player_1.description)
                    print('- '*30)


                    print(f"\nTurno de {player_1.get_name}")
                    print("Deseja receber uma nova carta ou permanecer?")
                    print("\n\t[1] Receber mais uma carta\n\t[ENTER] Permanecer\n")
                    option = input('...')
                    if option == '1':
                        player_1.add_card(deck.deal_one())
                    else:
                        player_1_turn = False
                        break

                if round_over:
                    break

                player_2_turn = True
                while player_2_turn:

                    if player_2.get_sum > 21:
                        if not player_2.ace_save():
                            round_over = True
                            player_1.win_round()
                            player_2.lose_round()
                            player_2_turn = False
                            sys("cls")
                            print(f"Rodada {turn}")
                            print('- '*30)
                            print(player_1)
                            print('- '*30)
                            if self.multiplayer:
                                print(player_2.description)
                            else:
                                print(player_2.dealer_print(play_state=True))
                            print('- '*30)
                            last_round = f"\nVencedor da última rodada: {player_1.get_name}\n"
                            print(f"\n\nVencedor: {player_1.get_name}")
                            input('\n[ENTER] Prosseguir...\n')
                            break
                    if player_2.get_sum == 21:
                        player_2.add_blackjack()

                    sys("cls")
                    print(f"Rodada {turn}")
                    print('- '*30)
                    print(player_1)
                    print('- '*30)
                    if self.multiplayer:
                        print(player_2.description)
                    else:
                        print(player_2.dealer_print(play_state=True))
                    print('- '*30)

                    print(f"\nTurno de {player_2.get_name}")
                    if self.multiplayer:
                        print("Deseja receber uma nova carta ou permanecer?")
                        print("\n\t[1] Receber mais uma carta\n\t[ENTER] Permanecer\n")
                        option = input('...')
                        if option == '1':
                            player_2.add_card(deck.deal_one())
                        else:
                            player_2_turn = False
                            break
                    else:
                        print("\n\t[ENTER] Executar dealer\n")
                        option = input('...')

                        if player_2.get_sum == 21 and player_2.get_sum == player_1.get_sum:
                            player_2.add_blackjack()
                            player_2_turn = False
                            last_round = "\nResultado da última rodada: Empate\n"
                            player_2.draw()
                            player_1.draw()
                            round_over = True
                            print("\n\nEmpate!")
                            input('\n[ENTER] Prosseguir...\n')
                            break
                        if player_2.get_sum <= player_1.get_sum:
                            player_2.add_card(deck.deal_one())
                        else:
                            player_2_turn = False
                            round_over = True
                            player_2.win_round()
                            player_1.lose_round()
                            last_round = f"\nVencedor da última rodada: {player_2.get_name}\n"
                            print(f"\n\nVencedor: {player_2.get_name}")
                            input('\n[ENTER] Prosseguir...\n')
                            break

                if self.multiplayer and not round_over:
                    if player_1.get_sum == player_2.get_sum:
                        player_1.draw()
                        player_2.draw()
                        last_round = "\nResultado da última rodada: Empate\n"
                        print("\n\nEmpate!")
                        input('\n[ENTER] Prosseguir...\n')
                        round_over = True
                        break

                    if player_1.get_sum > player_2.get_sum:
                        player_1.win_round()
                        player_2.lose_round()
                        last_round = f"\nVencedor da última rodada: {player_1.get_name}\n"
                        print(f"\n\nVencedor: {player_1.get_name}")
                        input('\n[ENTER] Prosseguir...\n')
                        round_over = True
                        break

                    player_2.win_round()
                    player_1.lose_round()
                    last_round = f"\nVencedor da última rodada: {player_2.get_name}\n"
                    print(f"\n\nVencedor: {player_2.get_name}")
                    input('\n[ENTER] Prosseguir...\n')
                    round_over = True
                    break

            turn += 1

        sys('cls')
        print(f"\n\nJogo encerrado! {winner.get_name} levou seu oponente à falência!")
        print(f"\n\tRodadas:\t\t{turn}")
        print(f"\tApostas circuladas:\t{player_1.get_bet_counter*2}")
        print(f"\tPor jogador:\t\t{player_1.get_bet_counter}\n")
        print('- '*30)
        print(f"\nEstatísticas de {player_1.get_name}:")
        print(f"\tVitórias:\t\t{player_1.get_wins}")
        print(f"\tDerrotas:\t\t{player_1.get_losses}")
        print(f"\tEmpates:\t\t{player_1.get_draws}")
        print(f"\tCartas recebidas:\t{player_1.get_card_counter}")
        print(f"\tContagem de 21:\t\t{player_1.get_blackjacks}")
        print(f"\tSaldo final:\t\t{player_1.get_bank}\n")
        print('- '*30)
        print(f"\nEstatísticas de {player_2.get_name}:")
        print(f"\tVitórias:\t\t{player_2.get_wins}")
        print(f"\tDerrotas:\t\t{player_2.get_losses}")
        print(f"\tEmpates:\t\t{player_2.get_draws}")
        print(f"\tCartas recebidas:\t{player_2.get_card_counter}")
        print(f"\tContagem de 21:\t\t{player_2.get_blackjacks}")
        print(f"\tSaldo final:\t\t{player_2.get_bank}\n")
        print('- '*30)
