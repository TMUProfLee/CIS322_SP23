from testing_base import *
import random

def start_player_info():

    game = GoFish()
    info = game.multiplayer_info()
    game.point_tracker_interface(info)

    deck = Deck()
    dealer = Dealer(deck)
    dealer.dealCards(5, game.players)
    for player in game.players:
      print("\n",player)
      player.showHand(player.hand)


start_player_info()