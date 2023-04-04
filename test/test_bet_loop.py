from testing_base import *

# Create deck
deck = Deck()
# Create dealer
dealer = Dealer(deck)

# Create players
matthew = Player('Matthew')
mark = Player('Mark')
luke = Player('Luke')
john = Player('John')
peter = Player('Peter')
players = [matthew, mark, luke, john, peter]

# Deal 2 cards to each player
dealer.dealCards(2, players)

# add money to each player
for player in players:
    player.addMoney(100)

# display player money before betting
print("=======================")
print("Totals before betting:")
for player in players:
    print(player.name, player.money)

# create and display Pot
pot = Pot(0)
print("Pot total before betting:")
print(pot.money)
print("=======================")

# run game
output = Play(dealer, players, pot)

# display player money after betting
print("=======================")
print("Totals after betting:")
for player in output:
    print(player.name, player.money)

# display Pot after betting
print("Pot total after betting:")
print(pot.money)
print("=======================")