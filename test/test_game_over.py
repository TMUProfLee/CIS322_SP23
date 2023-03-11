from testing_base import *
import random

def test_game_over():
    camila = Player('Camila')
    kaylie = Player('Kaylie')
    john = Player('John')
    players = [camila, kaylie, john]

    game = GoFish(players)
    deck = Deck()
    dealer = Dealer(deck)
    dealer.dealCards(5, players[0:2])
    for player in players:
      player.showHand(player.hand)
    game.ask_card()
    
test_game_over()
