from testing_base import *

#Create deck
deck = Deck()

#Create Dealer
dealer = Dealer(deck)

#Create Players
Matthew = Player("Matthew")
Mark = Player("Mark")
Luke = Player("Luke")
John = Player("John")
players = [Matthew, Mark, Luke, John]

#Deal cards
dealer.dealCards(3, players)

#Assert that bust function accurately checks if the hand's total is over 21
for player in players:
    if player.calculateHand() > 21:
        assert player.bust() == True
    elif player.calculateHand() <= 21:
        assert player.bust() == False
