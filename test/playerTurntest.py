from testing_base import *

def test_same_player_turn():
    # Setup
    players = ["Player 1", "Player 2", "Player 3"] 
    current_player = players[0]
    getCard = False

    # Execution
    player = playerTurn(players, current_player, getCard)

    # Assertion
    assert player == players[0]

def test_next_player_turn():
    # Setup
    players = ["Player 1", "Player 2", "Player 3"] 
    current_player = players[0]
    getCard = True

    # Execution
    player = playerTurn(players, current_player, getCard)
    playerTurn()

    # Assertion
    assert player == players[1] 





