from testing_base import *

# Create a deck to use
deck = Deck()
# Create a dealer
dealer = Dealer(deck)

# Create players for your game
players = {}
NumPlayers = int(input("Enter player count: "))
for i in range(1, NumPlayers+1):
    name = input("Player {} name: ".format(i))
    players = [Player(name)]

# Deal 5 cards to each player
dealer.dealCards(5, players)

# Show each player's hand
for player in players:
    print(f'{player.name}:')
    player.showHand(True)
    print()