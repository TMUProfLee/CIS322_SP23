import random
import os

cardImages = []
values = [11,2,3,4,5,6,7,8,9,10,10,10,10] # blackjack card values
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

def find_root_dir():
  cwd = os.getcwd()
  while 'source' not in os.listdir():
    os.chdir('..')
    cwd = os.path.join( cwd, '..')
  return cwd
import Card_Class
import Betting_Box_Class
import Dealer_Class
import Deck_Class
import Player_Class



class Deck:
  def __init__(self):
    root_dir = os.path.join( find_root_dir(), 'source')
    cards_file = f'{root_dir}{os.path.sep}playing_cards.txt'
    with open(cards_file, "r") as cards:
      cardBack = []
      for _ in range(6):
        line = cards.readline()
        cardBack.append(line.replace("\n",""))
      card = []
      level = 0
      for line in cards.readlines():
        if len(line) == 1:
          cardImages.append(card)
          level = 0
          card = []
          continue
        card.append(line.replace("\n",""))
        level += 1
      cardImages.append(card)
    
    deck = []
    index = 0
    for suit in suits:
      for value in values:
        deck.append(Card(suit, value, cardImages[index], cardBack))
        index += 1
    
    self.cards = deck
    self.size = len(deck)
    self.cardBack = cardBack
    self.discarded = []

  def reset(self):
    self.cards += self.discarded
    self.discarded = []
    self.size = len(self.cards)

  def shuffle(self):
    random.shuffle(self.cards)

  def getCard(self):
    card = self.cards.pop()
    self.size -= 1
    self.discarded.append(card)
    return card

def getCard(suit, value):
  deck = Deck()
  my_card = Card( suit.capitalize(), value, None, None)
  for card in deck.cards:
    if card == my_card:
      return card
  return None
class betting_box:
  def __init__(self, money: int = 0):
    self.wager = money
    self.betters= []

  def bet(self, bet, player: bool = False):
    if player:
      self.betters.append(player)
    for aBetter in self.betters:
      if aBetter.money >= bet:
        aBetter.makeBet(bet)
        self.wager += bet
      else:
        print(f'{aBetter.name} bet {bet} but only has {aBetter.money}')

  def collect(self, win, odds: int = 2):
    if win == -1:
      pass
    elif win == 1:
      for aBetter in self.betters:
        aBetter.addMoney(self.wager*odds/len(self.betters))
    else:
      for aBetter in self.betters:
        aBetter.addMoney(self.wager/len(self.betters))
    self.wager=0