from testing_base import *

name = "jonny"
player = Player(name, 50)
player_list = [player]
pot = Pot(100)
showWinner(player_list, pot)
Player.display(player)