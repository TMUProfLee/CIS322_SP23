from testing_base import *

# Create a deck to use
deck = Deck()

# Create pot
pot = Pot(10)

jesse = Player("Jesse", 2)

def test_create_pot():
    assert pot.money == 10
    assert jesse.money == 2

def test_add_to_pot():
    pot.addPot(2, jesse)
    assert pot.money == 12
    assert jesse.money == 0

def test_draw_from_pot():
    pot.rewardPot(jesse)
    assert pot.money == 0
    assert jesse.money == 12

def test_add_with_no_money():
    broke_jesse = Player("Jesse but he's a college student", 0)
    pot.addPot(2, broke_jesse)
    assert pot.money == 0 # in this case the player has no money so we shouldn't allow this transaction to occur
    assert broke_jesse.money == 0 # make sure we don't end up with a negative or anything weird