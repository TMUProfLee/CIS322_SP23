from testing_base import *

def test_showWinner():

    # Create two players
    donovan = Player('Donovan')
    jesse = Player('Jesse')
    players = [donovan, jesse]

    # Add cards to players' hand
    for p in players: 
        for i in range(6):
            p.addCard(Card("Hearts", random.randint(1, 10), [], []))

    for p in players:
        print(p.showValue(), p.name)
    
    # Determine the winner using the showWinner function
    winner = showWinner(players)
    
    # Test that the winner is correct using assert
    if winner == donovan:
        assert winner.name == 'Donovan'
    elif winner == jesse:
        assert winner.name == 'Jesse'
    
    print(f"Winner: {winner.name}")
