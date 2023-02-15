
from source import CardGames
from testing_base import *

deck = [
    Card("Hearts", 1, [], []),
    Card("Hearts", 2, [], []),
    Card("Hearts", 3, [], []),
    Card("Hearts", 4, [], []),
    Card("Hearts", 5, [], []),
]

donovan = CardGames.Player('Donovan')

caseVal = 15

for card in deck:
    donovan.addCard(card)

print('Test Passed') if caseVal == donovan.showValue() else print ('Test Failed') 

