players = ["Player 1", "Player 2", "Player 3"] 
current_player = players[0]
getCard = False  

def playerTurn(players, current_player, getCard):
    num_players = len(players)
    if getCard == True:
        return current_player
    else:
        next_player_index = (players.index(current_player) + 1) % num_players
        next_player = players[next_player_index]
        return next_player

print(playerTurn(players, current_player, getCard)) 

getCard = True    
def playerTurn(players, current_player, getCard):
    num_players = len(players)
    if getCard == True:
        return current_player
    else:
        next_player_index = (players.index(current_player) + 1) % num_players
        next_player = players[next_player_index]
        return next_player

print(playerTurn(players, current_player, getCard)) 
