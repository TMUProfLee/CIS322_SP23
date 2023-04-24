from testing_base import *

def test1():
    # Setup
    players = ["Player 1", "Player 2", "Player 3"] 
    current_player = players[0]
    drawCard = False

    # Execution
    player = nextPlayer(players, current_player, drawCard)

    # Assertion
    assert player == players[0]

def test2():
    # Setup
    players = ["Player 1", "Player 2", "Player 3"] 
    current_player = players[0]
    drawCard = True

    # Execution
    player = nextPlayer(players, current_player, drawCard)

    # Assertion
    assert player == players[1]


