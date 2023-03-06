from testing_base import *

# Create deck and dealer
deck = Deck()
dealer = Dealer(deck)

# Create players
players = {}
while True:
    try:
        NumPlayers = int(input("Enter player count: "))
        break
    except ValueError:
        print("Please enter number of players: ")
for i in range(1, NumPlayers+1):
    name = input("Player {} name: ".format(i))
    players[name] = Player(name)

# Deal 5 cards to each player
dealer.dealCards(5, list(players.values()))

# Show each player's hand
for player in players.values():
    print(f'{player.name}:')
    player.showHand(True)
    print()
