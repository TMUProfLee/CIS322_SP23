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

class Betting_box:
  def __init__(self, money: int = 0, betters = []):
    self.wager = money
    self.betters = betters

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
    if win == 1:
      pass
    elif win == 2:
      for aBetter in self.betters:
        aBetter.addMoney(self.wager*odds/len(self.betters))
    else:
      for aBetter in self.betters:
        aBetter.addMoney(self.wager/len(self.betters))
    self.wager=0