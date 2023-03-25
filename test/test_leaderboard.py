from testing_base import *

def test_leaderboard():

    donovan = Player('Donovan')
    jesse = Player('Jesse')
    players = [donovan, jesse]

    for p in players: 
        for i in range(6):
            p.addCard(Card("Hearts", random.randint(1, 10), [], []))

    for p in players:
        print(p.showValue(), p.name)


    winner = showWinner(players)
    print ('Winner: %s' %(winner.name))
    
    
    updateLeaderboard(winner)

    showLeaderboard(wins)
 
test_leaderboard()
test_leaderboard()
    
