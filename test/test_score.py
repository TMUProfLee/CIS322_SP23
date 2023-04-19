from testing_base import *

def test_score_0():
    # create a game object
    game = GoFish()
    
    # add two players to the game
    alice = Player('Alice')
    bob = Player('Bob')

    game.players = [alice, bob]
    game.player_turn = alice

    # set up the players' hands to have one matching pair each
    game.players[0].hand = [getCard("Hearts", 3), getCard('Diamonds', 3), getCard("Clubs", 5), getCard("Spades", 10), getCard("Spades", 13)]
    game.players[1].hand = [getCard("Clubs", 2), getCard('Diamonds', 5), getCard("Hearts", 2), getCard("Spades", 7), getCard("Hearts", 12)]

    # make sure the initial score is zero
    assert game.score() == 0


def test_score_1():
    # create a game object
    game = GoFish()
    
    # add two players to the game
    alice = Player('Alice')
    bob = Player('Bob')

    game.players = [alice, bob]
    game.player_turn = alice

    game.score()

    # set up the players' hands to have one matching pair each
    game.players[0].hand = [getCard("Hearts", 3),getCard('Diamonds', 3), getCard("Clubs", 3), getCard("Spades", 3), getCard("Spades", 13)]
    
    game.players[1].hand = [getCard("Clubs", 2), getCard('Diamonds', 5), getCard("Hearts", 2), getCard("Spades", 7), getCard("Hearts", 12)]
    
    # make sure the initial score is zero
    assert game.score() == 1