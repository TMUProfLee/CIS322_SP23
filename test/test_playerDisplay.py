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
    player.display()

#Create player with no cards
john = Player('John')

#test behavior for player with no cards
john.display()

#Add money to player
john.addMoney(45)

#Test if player money is updated
john.display()