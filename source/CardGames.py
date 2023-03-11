import random
import os
import sys
import time
sys.path

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

  def game_over(self):
    j = 0
    gm = ["G", "A", "M", "E", "O", "V", "E","R"]
    for i in range(20):
      print(" "*j, ".")
      j += 3
      if i == 10:
        for i in range (len(gm)):
          print(" "*j, gm[i])
          j += 3

    sys.exit()
    


    
  def player_deck_info(self):
    for i in range(len(self.players)):
      self.playerinfo.append([])

    for i in range(len(self.players)):
      self.playerinfo[i].append(self.players[i])
      self.playerinfo[i].append(self.players[i].hand)
    return self.playerinfo

  def index(self, player_wanted, info):
    for i in range(len(info)):
      player = info[i][0]
      if str(player_wanted) == str(player):
        return i

  def surrender_card(self):
    temp_list1 = []
    counter = 0
    for i in self.info_player_asked:
      if str(i) != str(self.value_wanted):
        counter += 1 
      else:
        temp_list1.append(self.info_player_asked[counter])
        self.player_turn.addCard(temp_list1[0])
        del self.info_player_asked[counter]
        if len(self.info_player_asked) == 0:
          self.game_over()
        

    
    
        

    print(self.player_turn)
    self.player_turn.showHand()
    print(self.player_asked)
    self.player_asked.showHand()


  def ask_card(self):
    self.player_deck_info()
    player_turn = input(str("What is your name? "))
    player_asked = input(str("Who would like to ask? "))

    self.value_wanted = int(input("What value would you like? "))
  
    self.info_player_turn = self.playerinfo[self.index(player_turn, self.playerinfo)][1]
    self.info_player_asked = self.playerinfo[self.index(player_asked, self.playerinfo)][1]

    self.player_turn = self.playerinfo[self.index(player_turn, self.playerinfo)][0]
    self.player_asked = self.playerinfo[self.index(player_asked, self.playerinfo)][0]
    
    
    self.surrender_card()


  


          
      

    


      



  
 