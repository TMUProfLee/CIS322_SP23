import random
import os
import sys
import time

cardImages = []
values = list(range(1,14))
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

def find_root_dir():
  cwd = os.getcwd()
  while 'source' not in os.listdir():
    os.chdir('..')
    cwd = os.path.join( cwd, '..')
  return cwd

class Card:
  def __init__(self, suit, value, image, cardBack):
    self.cardBack = cardBack
    self.suit = suit
    self.value = value
    self.image = image
    self.shortImage = []
    for line in self.image:
      self.shortImage.append(line[:4])
    
  def __str__(self):
    return f'{self.value}'

  def __eq__(self, other):
    if not type(other) == Card:
      return False
    return self.suit == other.suit and \
      self.value == other.value
  def __str__(self):
    return str(self.value)
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

def getCard( suit, value):
  deck = Deck()
  my_card = Card( suit.capitalize(), value, None, None)
  for card in deck.cards:
    if card == my_card:
      return card
  return None

####################################################################################
def count_cards(deck):
  #How many cards are in the deck assigned to "num_cards"
  num_cards = len(deck)
  #For each iteration the number of cars in the deck decrease by 1 card
  for i in range(num_cards):
    print("There are "+ str(num_cards - i) +" more cards in the deck")
#####################################################################################
class Player:
  def __init__(self, name, money: int = 0):
    self.name = name
    self.hand = []
    self.knownCards = []
    self.money = money
    
  def __str__(self):
    return (str(self.name))

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

  def setHand(self, cards: "list[Card]", isKnown: bool = False):
    self.hand = cards
    self.knownCards = [isKnown for _ in self.hand]

  #function
  def MatchFour(self):
    for i in range(len(self.hand)):
      for j in range(i + 1, len(self.hand)):
        for k in range(j + 1, len(self.hand)):
          for l in range(k + 1, len(self.hand)):
            if self.hand[i].value == self.hand[j].value == self.hand[k].value == self.hand[l].value:
              print("You have a set of %ss!" % self.hand[i].value)
              return True
    return False

  def showHand(self, printShort: bool = False):
    add = []
    for idx in range(6):
      for i, card in enumerate(self.hand):
        if printShort and i < len(self.hand)-1:
          image = card.shortImage[idx]  if self.knownCards[i] else card.cardBack[idx]
          
          print(image, end="")
        else:
          image = card.image[idx] if self.knownCards[i] else card.cardBack[idx]
          print(image, end="")
       # print(card)
        if idx == 0:
          add.append(str(card))
        if idx == 5:
          add = list(map(int, add))
        
      print()
    return sum(add)
    
    
  def High(self):
    l =[]
    l2 =[]
    for c in self.hand:
      l.append(str(c))
    for c in l:
      l2.append(int(c))
    x = max(l2)
    print(x)

  def clearHand(self):
    self.hand = []
    self.knownCards = []
  
  ##MY FUNCTION##

  def printHand(self):
    list1 = []
    for i in self.hand:
      list1.append(str(i))
    return list(map(int, list1))

  def get_playerHand(self):
    print()

  def addValues(self):
    list1 = []
    #Creates empty list
    for i in self.hand:
      #print(i)
      #gets each value of card that is found in self.hand
      list1.append(str(i))
      #appends the value as string to a list
    integer_list = list(map(int, list1))
    #converts all strings in list into integer
    return sum(integer_list)

  def PairHand(self):
      pairs = []
      for i in range(len(self.hand)):
          for j in range(i + 1, len(self.hand)):
              if self.hand[i].value == self.hand[j].value:                    
                if self.hand[i].value not in pairs:
                  pairs.append(self.hand[i].value)
      if pairs:
          print(f"You have a pair of {pairs[0]}'s")
      else:
          print("You do not have a pair")         
      return pairs


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

  def printHands(self, players: dict):
    # Show each player's hand
    for player in players.values():
        print(f'{player.name}:')
        player.showHand(True)
        print() 


class GoFish:
  def __init__(self, players: "list[Player]"):
    self.playerinfo = []
    self.players = players
    self.value_wanted = int
    self.suit_wanted = ""
    self.player_asked = ""
    self.player_turn = ""
    self.info_player_turn = int
    self.info_player_asked = int

  def start_game(self):
    deck = Deck()
    dealer = Dealer(deck)
    dealer.dealCards(5, self.players)
    for player in self.players:
      player.showHand(player.hand)
    
  def player_deck_info(self):
    for i in range(len(self.players)):
      self.playerinfo.append([])

    for i in range(len(self.players)):
      self.playerinfo[i].append(self.players[i])
      self.playerinfo[i].append(self.players[i].hand)
    #print(self.playerinfo)
    return self.playerinfo

  def index(self, player_wanted, info):
    for i in range(len(info)):
      player = info[i][0]
      if str(player_wanted) == str(player):
        return i

  def surrender_card(self):
    temp_list1 = []
    temp_list2 = []
    counter = 0
    for i in self.info_player_asked:
      print(str(i), i.suit)
      
      if str(i) != str(self.value_wanted):
        counter += 1 
      elif i.suit != str(self.suit_wanted):
        counter += 1
      else:
        temp_list1.append(self.info_player_asked[counter])
        self.player_turn.addCard(temp_list1[0])
        
        for i in range(len(self.info_player_asked)):
          card = self.info_player_asked.pop()
          if str(card) != str(self.value_wanted):
            temp_list2.append(card)
          elif card.suit != str(self.suit_wanted):
            temp_list2.append(card)

        for i in range(len(temp_list2)):
          self.info_player_asked.append(temp_list2[i])

    print(self.player_turn)
    self.player_turn.showHand()
    print(self.player_asked)
    self.player_asked.showHand()


  def ask_card(self):
    self.player_deck_info()
    player_turn = input(str("What is your name? "))
    player_asked = input(str("Who would like to ask? "))

    self.value_wanted = int(input("What value would you like? "))
    self.suit_wanted = str(input("What suit would you like? "))

    self.info_player_turn = self.playerinfo[self.index(player_turn, self.playerinfo)][1]
    self.info_player_asked = self.playerinfo[self.index(player_asked, self.playerinfo)][1]

    self.player_turn = self.playerinfo[self.index(player_turn, self.playerinfo)][0]
    self.player_asked = self.playerinfo[self.index(player_asked, self.playerinfo)][0]

    self.surrender_card()
def question():
  x = input('It is your turn who whould you like to ask? ')
  y = input('what card would you like to ask that player for?')
  if x == 'p1':
    print('pass the computer to p1')
    print('\n\n\n\n\n\n\n\n\n\n\n\n')
    time.sleep(10) 
    print('do you have', y, "?")
    z = input('do you have one?')
    if y == 'yes':
      #give card
      print('player has card')
    elif y == 'no':
      print('Go fish')
  if x == 'p2':
    print('pass the computer to p2')
    print('\n\n\n\n\n\n\n\n\n\n\n\n')
    time.sleep(10) 
    print('do you have', y, "?")
    z = input('do you have one?')
    if y == 'yes':
      #give card
      print('player has card')
    elif y == 'no':
      print('Go fish')
  if x == 'p3':
    print('pass the computer to p3')
    print('\n\n\n\n\n\n\n\n\n\n\n\n')
    time.sleep(10) 
    print('do you have', y, "?")
    z = input('do you have one?')
    if y == 'yes':
      #give card
      print('player has card')
    elif y == 'no':
      print('Go fish')
  if x == 'p4':
    print('pass the computer to p4')
    print('\n\n\n\n\n\n\n\n\n\n\n\n')
    time.sleep(10) 
    print('do you have', y, "?")
    z = input('do you have one?')
    if y == 'yes':
      #give card
      print('player has card')
    elif y == 'no':
      print('Go fish')
question()
