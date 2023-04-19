def player_ages(players):
    playerAge = []
    for player in players.values():
        while True:
            try:
                age = int(input("Enter {}'s age: ".format(player.name)))
                playerAge.append((player, age))
                break
            except ValueError:
                print("Please enter a valid age: ")
    playerAge = sorted(playerAge, key=lambda x: x[1])
    youngestPlayer = playerAge[0][0]
    print("{} goes first!\n".format(youngestPlayer.name))
    return [p for p, _ in playerAge]