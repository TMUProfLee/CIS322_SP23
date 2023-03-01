from testing_base import *


# Create a deck to use
deck = Deck()
# Create a dealer
dealer = Dealer(deck)


# Create players for your game
matthew = Player('Matthew')
mark = Player('Mark')
donovan = Player('Donovan')
players = [matthew, mark, donovan]

# Deal 5 cards to each player
dealer.dealCards(2, players)




# Show each player's hand and hand value
for player in players:
    print(f'{player.name}:')
    print(f'Hand Value: {player.showValue()}')
    player.showHand(True)
    print()    

