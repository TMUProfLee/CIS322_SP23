def MultPlayer():
    players = {}
    NumPlayers = int(input("Enter player count: "))
    for i in range(1, NumPlayers+1):
        name = input("Player {} name: ".format(i))
        players[i] = name

print(players)


     
            
        
