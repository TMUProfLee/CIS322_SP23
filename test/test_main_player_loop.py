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

output = Play(dealer, players)

#assert output type is a list
assert type(output) == list

#assert that items in list are players and that players have not busted
for player in output:
    assert type(player.name) == str
    assert player.bust() == False



