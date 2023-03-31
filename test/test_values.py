from testing_base import *

def test_values():
    deck = Deck()
    dealer = Dealer(deck)
    matthew = Player('Matthew')
    mark = Player('Mark')
    jane = Player('Jane')
    toby = Player('Toby')
    camila = Player('Camila')
    kaylie = Player('Kaylie')
    players = [matthew, mark, jane, toby, camila, kaylie]
    dealer.dealCards(5, players)

    for player in players:
        print('\n\n',f'{player.name} {player.addValues()}:')
        player.addValues()
        

        assert print(player.showHand(True)) == print(player.addValues())

test_values()

