def printHands(players: dict):
    # Show each player's hand
    for player in players.values():
        print(f'{player.name}:')
        player.showHand(True)
        print() 
    



     
            
        
