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

class Dealer:
  def __init__(self, deck: Deck):
    self.deck = deck
    self.deck.shuffle()

  def printCards(self, cards: "list[Card]", showFront: bool, printShort: bool = True):
    for idx in range(6):
      for i, card in enumerate(cards):
        if printShort and i < len(cards)-1:
          image = card.shortImage[idx] if showFront else card.cardBack[idx]
          print(image, end="")
        else:
          image = card.image[idx] if showFront else card.cardBack[idx]
          print(image, end="")
      print()

  def dealCards(self, numCards: int, players: "list[Player]"):
    if numCards * len(players) > self.deck.size:
      return False
    for player in players:
      for _ in range(numCards):
        player.addCard(self.deck.getCard())
    return True

  def resetDeck(self):
    self.deck.reset()
    self.deck.shuffle()

# simple respond for dealer in single player with known hands 
def dealerHand(dealer, house, player):
  houseHand = house.handSum()
  playerHand = player.handSum()
  if playerHand == 21 and len(player.hand) == 2: #if blackjack then player auto win
    return 1   
  if houseHand == 21 and len(house.hand) == 2: #if blackjack then house auto win
    return -1 
  while houseHand < 17: #force hit when below 17
    dealer.dealCards(1, [house])
    houseHand = house.handSum()

  if playerHand <= 21: 
    while playerHand >= houseHand: # keep hitting until house hand value is bigger than player hand, unless houseHand reach 21
      if playerHand == houseHand and houseHand >=19:
        break
      dealer.dealCards(1, [house])
      houseHand = house.handSum()
  
  if playerHand == houseHand:
    return 0
  if playerHand > 21 and houseHand > 21:
    return 0
  if playerHand > houseHand:
    return 1 if playerHand <= 21 else -1

  if houseHand > playerHand:
    return -1 if houseHand <= 21 else 1