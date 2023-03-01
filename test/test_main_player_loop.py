from testing_base import *
import pytest

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
@pytest.mark.parametrize("out",output)

#This verifies that a list is returned, each list item is a player type, and that each player did not bust
def test_player_bust(out):
  assert out.bust() == False

for i in range(len(output) - 1):
  test_player_bust(output[i])


