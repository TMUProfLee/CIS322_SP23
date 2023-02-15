from testing_base import *

def test_PairHand():
    # Create a deck to use
    deck = Deck()
    # Create a dealer
    dealer = Dealer(deck)

    # Create players for your game
    matthew = Player('Matthew')
    mark = Player('Mark')
    players = [matthew, mark]

    # Deal 5 cards to each player
    dealer.dealCards(5, players)

    # Show each player's hand
    for player in players:
        print(f'{player.name}:')
        player.showHand(True)
        player.PairHand()
        print()
