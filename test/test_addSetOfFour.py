from testing_base import *

"""def test_addSetOfFour(player):
  player = Player("Alice")
  player.hand = [Card("Spades", 2), Card("Hearts", 2), Card("Diamonds", 2), Card("Clubs", 2)]
  player.addSetOfFour(2)
  self.assertEqual(player.setsOfFour[2], 1)

  player.hand = [Card("Spades", 2), Card("Hearts", 2), Card("Diamonds", 2), Card("Clubs", 2), Card("Spades", 3)]
  player.addSetOfFour(2)
  self.assertEqual(player.setsOfFour[2], 2)

  player.hand = [Card("Spades", 2), Card("Hearts", 2), Card("Diamonds", 2), Card("Clubs", 3), Card("Spades", 3)]
  player.addSetOfFour(2)
  self.assertEqual(player.setsOfFour[2], 2)"""

def test_addSetOfFour():
    obj = Player("John")
    obj.addSetOfFour(1)
    obj.addSetOfFour(2)
    obj.addSetOfFour(2)
    obj.addSetOfFour(3)
    assert obj.setsOfFour == {1: 1, 2: 2, 3: 1} # Test case 1
    
    obj.addSetOfFour(1)
    obj.addSetOfFour(2)
    obj.addSetOfFour(2)
    obj.addSetOfFour(3)
    assert obj.setsOfFour == {1: 2, 2: 4, 3: 2} # Test case 2

