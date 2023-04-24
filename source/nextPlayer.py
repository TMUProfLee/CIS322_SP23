def nextPlayer(players, current_player, drawCard):
    #creates an array out of players. 
    num_players = len(players)
    if drawCard:
        #if a card is drawn the turn goes to the next player in the array. 
        next_player = (current_player + 1) % num_players
        return next_player
    else:
        #if a card isn't drawn the player goes again. 
        return current_player

