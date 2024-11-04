# Arquivo principal a ser executado para jogar
# Desenvolvido por Zac Milioli
from blackjack import Game

if __name__ == "__main__":
    # game = Game(player_1="Zac", player_1_bank=100, player_2="Insira o nome aqui",
    #             player_2_bank=100, multiplayer=True)
    game = Game(player_1="Zac")
    game.run()
