from testing_base import *

Matthew = Player("Matthew")
deck = Deck()
pot = Pot(1)
ace_of_hearts = deck.cards[26]
Matthew.addCard(ace_of_hearts)
    
def test_play_game_works():
    guesses = playMiniGame(pot)
    assert(pot.money == guesses or (guesses == 0 and pot.money == 1))
