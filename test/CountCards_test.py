from testing_base import *
def test_count_cards(capsys):
    deck = ['Ace of Spades', 'Two of Hearts', 'Three of Clubs', 'Four of Diamonds']
    count_cards(deck)
    captured = capsys.readouterr()
    assert captured.out == "There are 4 more cards in the deck\nThere are 3 more cards in the deck\nThere are 2 more cards in the deck\nThere are 1 more cards in the deck\n"
    
    empty_deck = []
    count_cards(empty_deck)
    captured = capsys.readouterr()
    assert captured.out == "The deck is now empty. Game over, Thanks for playing!\n"
