def playerTurn(players, current_player, getCard):
    num_players = len(players)
    if getCard:
        return current_player
    else:
        next_player = (current_player + 1) % num_players
        return next_player 