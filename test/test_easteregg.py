from testing_base import *

Matthew = Player("Matthew")
deck = Deck()

def test_zero_cards():
    assert(checkIfEasterEgg(Matthew) == False)

def test_ace_of_hearts():
    ace_of_hearts = deck.cards[26]
    Matthew.addCard(ace_of_hearts)
    assert(checkIfEasterEgg(Matthew))
