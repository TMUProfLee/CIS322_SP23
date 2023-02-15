from testing_base import *

deck = Deck()
# Create a
dealer = Dealer(deck)

# Create players for your game
matthew = Player('Matthew')
mark = Player('Mark')
players = [matthew, mark]

# Deal 5 cards to each player

dealer.dealCards(5, players)

for player in players:
    player.display()