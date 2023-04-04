from testing_base import *

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



def test_printHand():
    # Create deck and dealer
    deck = Deck()
    dealer = Dealer(deck)

    # Create players
    players = {}
    while True:
        try:
            NumPlayers = int(input("Enter player count: "))
            break
        except ValueError:
            print("Please enter number of players")
    for i in range(1, NumPlayers+1):
        name = input("Player {} name: ".format(i))
        players[name] = Player(name)

    # Determine player order
    player_order = player_ages(players)

    # Deal 5 cards to each player in player order
    for player in player_order:
        dealer.dealCards(5, [player])

    # Show each player's hand
    printHands(players)

test_printHand()

