from testing_base import *

# Create a deck to use
deck = Deck()
# Create a dealer
dealer = Dealer(deck)

# Create player for your game
matthew = Player('Matthew')

def test_one_card():
    # deal one card, at which point we can't have a pair
    dealer.dealCards(1, [matthew])
    assert matthew.has_pair() == False

def test_two_cards():
    # after the first runs we have two cards, assert that has_pair returns true if the two cards match...
    # 12/13 times this will be false so this isn't the best test, but combined with the other two it'll get the job done
    dealer.dealCards(1, [matthew])
    assert matthew.has_pair() == (matthew.hand[0].value == matthew.hand[1].value)

def test_all_cards():
    # we now have all 52 cards, has to have pair
    dealer.dealCards(50, [matthew])
    assert matthew.has_pair() == True

