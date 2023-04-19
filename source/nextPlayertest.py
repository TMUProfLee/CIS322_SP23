players = ["Player 1", "Player 2", "Player 3"] #Test list of players
current_player = players[1]
getCard = True  #Current player decides to draw card

def playerTurn(players, current_player, getCard):
    num_players = len(players)
    if getCard:
        return current_player
    else:
        next_player = (current_player + 1) % num_players
        return next_player

