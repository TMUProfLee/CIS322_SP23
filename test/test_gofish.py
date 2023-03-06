from testing_base import *
import random

def test_gofish():
    camila = Player('Camila')
    kaylie = Player('Kaylie')
    john = Player('John')
    players = [camila, kaylie, john]


    info = [['Camila', [8, 7, 2, 8, 3]], ['Kaylie', [8, 3, 4, 9, 10]], ['John', [1, 5, 8, 2, 10]]]

    GoFish.start_game(0,players)
    print(GoFish.create_deckInfo(0, players))

    GoFish.ask_Card(0, 8, "Hearts", players, players[0])


test_gofish()
