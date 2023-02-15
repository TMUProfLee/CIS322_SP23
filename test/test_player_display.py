from testing_base import *

# Create a deck to use
deck = Deck()
# Create a dealer
dealer = Dealer(deck)

# Create players for your game
matthew = Player('Matthew')
mark = Player('Mark')
players = [matthew, mark]

# Deal 5 cards to each player
numCards = 5
dealer.dealCards(numCards, players)

def test_display():
    for player in players:

        assert type(repr(player.display())) == type('str') # check if the output is a string type