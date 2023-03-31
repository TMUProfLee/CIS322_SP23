from testing_base import *

def test_printCardsIfSet(capsys):
    player = Player("Test Player")
    player.addCard(Card("Hearts", 1, [], []))
    player.addCard(Card("Clubs", 1, [], []))
    player.addCard(Card("Diamonds", 1, [], []))
    player.addCard(Card("Spades", 1, [], []))

    player.printCardsIfSet()
    captured = capsys.readouterr()

    assert "You have a set of four 1's!" in captured.out
    assert "Would you like to print your hand? (Y/N)" in captured.out
    assert "1 of Hearts" in captured.out
    assert "1 of Clubs" in captured.out
    assert "1 of Diamonds" in captured.out
    assert "1 of Spades" in captured.out