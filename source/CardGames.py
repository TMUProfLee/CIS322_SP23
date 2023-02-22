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

  #def askCard(self, player_turn, player_asked, value, playerDeckinfo, players: "list[Player]"):
    


  def resetDeck(self):
    self.deck.reset()
    self.deck.shuffle()

class GoFish:
  def __init__(self, deck: Deck, players: "list[Player]"):
    self.deck = deck
    self. dealer = dealer

  def start_game(self, players):
    deck = Deck()
    dealer = Dealer(deck)
    dealer.dealCards(5, players)
    for player in players:
      player.showHand(player.hand)
  
  #adds name and deck to a list
  def create_deckInfo(self, players):
    playerDeckInfo = []
    for i in range(len(players)):
      playerDeckInfo.append([])
  
    #player names and deck/hand
    for i in range(len(players)):
      playerDeckInfo[i].append(players[i])
      playerDeckInfo[i].append(players[i].hand)
    return playerDeckInfo

  #gets index of name or card wanted
  def index(self, players, get_player_index):
    info = GoFish.create_deckInfo(self, players)
    for i in range(len(GoFish.create_deckInfo(self, players))):
      player = info[i][0]
      if str(get_player_index) == str(player):
        index_value = i
        return info[index_value]

  #when you have the card 
  def surrender_card(self, value_wanted, suit_wanted, p_turn, p_asked):
    list1 = [] 
    list2 = []
    counter = 0 
    #get_val
    #if value asked for is not in player deck
    for i in p_asked[1]:
      print(i.suit)
      print("(same value:", bool(str(i) == str(value_wanted)),")", "(same suit:",bool(i.suit == suit_wanted),")")
      if str(i) != str(value_wanted):
        counter += 1
      elif i.suit != str(suit_wanted):
        counter += 1
      
    #if it is, it will add that card to the player who asked and remove 
    #card from player who has to turn it in 
      else:
        #appends the card 
        list1.append(p_asked[1][counter])
        p_turn[0].addCard(list1[0])
      
        #pop from player deck to see if they have card
        #if its not the value the other player asked for
        #it adds it to a temp list
        #if it is, it does not add it to the temp list

        for i in range(len(p_asked[1])):
          a = p_asked[1].pop()
          #print(i, str(a), str(value_wanted))
          #print(bool(str(a) == str(value_wanted)), bool(a.suit == suit_wanted))
          if str(a) != str(value_wanted):
            list2.append(a)
          elif a.suit != str(suit_wanted):
            list2.append(a)


        #transfers temp list to the player deck 
        for i in range(len(list2)):
          p_asked[1].append(list2[i])
        
        print(p_asked[1])
        p_turn[0].showHand()
        p_asked[0].showHand()
        return 

  def ask_Card(self, value_wanted, suit_wanted, players, player_turn):
    #player_turn = GoFish.index(self, players, player_turn)
    player_asked = input("Who do you want to ask?: ")

    value_player_asked = GoFish.index(self, players, player_asked)
    value_player_turn = GoFish.index(self, players, "Camila")
    #print(value_player_turn)

    GoFish.surrender_card(self, value_wanted, suit_wanted, value_player_turn, value_player_asked)


    


