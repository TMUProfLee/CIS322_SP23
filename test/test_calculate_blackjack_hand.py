from testing_base import *

# Create a deck to use
deck = Deck()

# Create player for your game
matthew = Player('Matthew')

def test_zero_cards():
    assert matthew.calculateHand() == 0

def test_ace():
    matthew.addCard(deck.cards[0], True)
    assert matthew.calculateHand() == 11

def test_two_aces():
    matthew.addCard(deck.cards[0], True)
    assert matthew.calculateHand() == 12

def test_add_four():
    matthew.addCard(deck.cards[3], True)
    assert matthew.calculateHand() == 16