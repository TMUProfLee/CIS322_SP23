from testing_base import *

def test_leaderboard():

    donovan = Player('Donovan')
    jesse = Player('Jesse')
    players = [donovan, jesse]

    
    
    donovan.addCard(Card("Hearts", (5), [], []))
    donovan.addCard(Card("Hearts", (4), [], []))
    donovan.addCard(Card("Clubs", (3), [], []))

    jesse.addCard(Card("Hearts", (2), [], []))
    jesse.addCard(Card("Spades", (3), [], []))
    jesse.addCard(Card("Diamonds", (3), [], []))



    for p in players:
        print(p.showValue(), p.name)


    winner = showWinner(players)
    print ('Winner: %s' %(winner.name))
    
    
    updateLeaderboard(winner.name)

    showLeaderboard()
 
test_leaderboard()

    
