from testing_base import *

def test_dynamicLeaderboard():

    donovan = Player('Donovan')
    jesse = Player('Jesse')
    roy = Player('Roy')
    jonny = Player('Jonny')

    players = [donovan, jesse, roy, jonny]

    # Add cards to players' hand
    for p in players: 
        for i in range(6):
            p.addCard(Card("Hearts", random.randint(1, 10), [], []))

    for p in players:
        print(p.showValue(), p.name)
    
    winner = showWinner(players)

    print(f'\nWinner: {winner.name}!')
    updateLeaderboard(winner.name)
    showLeaderboard()

test_dynamicLeaderboard()