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
dealer.dealCards(5, players)

# Show each player's hand
for player in players:
    print(f'{player.name}:')
    player.showHand(True)
    print()
# checks for pairs and sets
for player in players:
    print(f'{player.name}:')
    for pair in player.pairCheck():
        print("There is a pair of",str(pair)+"'s")
    for setlist in player.matching():
        print("There are",setlist[1],str(setlist[0])+"'s")