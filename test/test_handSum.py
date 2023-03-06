from testing_base import *

#testing to see if the function adds the values correctly


deck = [ Card("Hearts", 1, [], []), Card("Hearts", 2, [], []), Card("Hearts", 3, [], []), Card("Hearts", 4, [], []), Card("Hearts", 5, [], [])
]

donovan = Player('Donovan')
caseVal = 15

def test_checkHandSum(user, case, cards):

      for card in cards:
          user.addCard(card)

      print('Test Passed') if user.showValue() == case else print ('Test Failed')

test_checkHandSum(donovan, caseVal, deck)

