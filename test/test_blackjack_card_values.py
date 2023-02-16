from testing_base import *

# Create a deck to use
deck = Deck()

def test_ace():
    ace = deck.cards[0]
    assert ace.value == 11

def test_five():
    five = deck.cards[4]
    assert five.value == 5

def test_eight():
    eight = deck.cards[7]
    assert eight.value == 8

def test_ten():
    ten = deck.cards[9]
    assert ten.value == 10

def test_king():
    king = deck.cards[12]
    assert king.value == 10