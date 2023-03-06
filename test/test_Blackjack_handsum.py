from testing_base import *

"""Player intializations"""
Grant = Player("Grant")
Jason = Player("Jason")
Mike = Player("Mike")
Arnold = Player("Arnold")

"""Player's hands"""
Grant.addCard(getCard("spades", 11)), Grant.addCard(getCard("spades", 11)) # two aces == 12
Jason.addCard(getCard("spades", 11)), Jason.addCard(getCard("spades", 11)), Jason.addCard(getCard("spades", 10)) # two aces and a facecard/10 == 12
Mike.addCard(getCard("spades", 10)), Mike.addCard(getCard("spades", 10)), Mike.addCard(getCard("spades", 10)) # three facecards/10 == 30
Arnold.addCard(getCard("spades", 11)), Arnold.addCard(getCard("spades", 10)) # ace and a facecard/10 (blackjack) == 21

"""player and value dictionary"""
players = {Grant:12,Jason:12,Mike:30,Arnold:21}

"""handSum() test"""
def test_Blackjack_handSum():
    for player in players:
        assert player.handSum() == players[player]

test_Blackjack_handSum()