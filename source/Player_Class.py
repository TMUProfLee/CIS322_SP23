import random
import os
import Card_Class
import Betting_Box_Class
import Dealer_Class
import Deck_Class
import Player_Class

cardImages = []
values = [11,2,3,4,5,6,7,8,9,10,10,10,10] # blackjack card values
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

def find_root_dir():
  cwd = os.getcwd()
  while 'source' not in os.listdir():
    os.chdir('..')
    cwd = os.path.join( cwd, '..')
  return cwd

class Player:
  def __init__(self, name, money: int = 0):
    self.name = name
    self.hand = []
    self.knownCards = []
    self.money = money
  
  def display(self):
    print("Name: " + self.name + "|| Money: " + str(self.money) + "|| Hand: " + str(self.handSum()))
    self.showHand(False)

  def addMoney(self, amount: int):
    self.money += amount
    return self.money

  def makeBet(self, amount: int):
    if amount > self.money:
      print("%s does not have enough money to make this bet." % self.name)
      return self.money
    self.money -= amount
    return self.money

  def addCard(self, card: Card, isKnown: bool = True):
    self.hand.append(card)
    if isKnown:
      self.knownCards.append(True)
    else:
      self.knownCards.append(False)

  def handSum(self):
    """Sums together the hand and adjusts the sum depending on the best value of an ace (11 or 1)"""
    handsum = 0
    aces = 0
    for card in self.hand:
      if card.value == 11:
        aces += 1
      handsum += card.value
    while aces > 0 and handsum > 21:
      aces -= 1
      handsum -= 10
    return handsum

  def setHand(self, cards: "list[Card]", isKnown: bool = False):
    self.hand = cards
    self.knownCards = [isKnown for _ in self.hand]

  def showHand(self, printShort: bool = False):
    for idx in range(6):
      for i, card in enumerate(self.hand):
        if printShort and i < len(self.hand)-1:
          image = card.shortImage[idx]  if self.knownCards[i] else card.cardBack[idx]
          print(image, end="")
        else:
          image = card.image[idx] if self.knownCards[i] else card.cardBack[idx]
          print(image, end="")
      print()
  def pairCheck(self):#returns a list of values that appear at least twice in the players hand
    pairlist=[]
    aVar1 = 0
    while aVar1 < len(self.hand) - 1:
      aVar2 = aVar1 + 1
      while aVar2 < len(self.hand) :
        #print(self.hand[aVar1].value,self.hand[aVar2].value)
        duplicateCheck = False
        for cardValue in pairlist:
          if cardValue == self.hand[aVar1].value:
            duplicateCheck = True
        if self.hand[aVar1].value == self.hand[aVar2].value and not duplicateCheck :
          pairlist.append(self.hand[aVar1].value)
        aVar2 += 1
      aVar1 += 1
    return(pairlist)

  def matching(self):
    report = []
    pairlist = self.pairCheck()
    for pairValue in pairlist:
      matches = 0
      for aCard in self.hand:
        if aCard.value == pairValue:
          matches += 1
      report.append([pairValue,matches])
    return report
  def clearHand(self):
    self.hand = []
    self.knownCards = []