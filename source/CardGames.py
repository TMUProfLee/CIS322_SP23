import random
import os

cardImages = []
values = [11,2,3,4,5,6,7,8,9,10,10,10]
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

def find_root_dir():
  cwd = os.getcwd()
  while 'source' not in os.listdir():
    os.chdir('..')
    cwd = os.path.join( cwd, '..')
  return cwd

def initializeGame():
  deck = Deck()
  dealer = Dealer(deck)
  pot = Pot(0)
  playerNames = []
  morePlayers = True
  buyIn = int(input("Enter buy-in ammount: "))
  while morePlayers:
    anotherPlayer = input("Add another player? (Y/N): ")
    if anotherPlayer == "Y" or anotherPlayer == "y":
      newPlayer = input("Enter name of new player: ")
      playerNames.append(newPlayer)
    else:
      morePlayers = False
  pot.addPot(buyIn * len(playerNames))
  pot.printPot()
  initPlayers = [] 
  for p in playerNames:
    initPlayers.append(Player(p))
  dealer.dealCards(2, initPlayers)
  return dealer, initPlayers, pot

class Card:
  def __init__(self, suit, value, image, cardBack):
    self.cardBack = cardBack
    self.suit = suit
    self.value = value
    self.image = image
    self.shortImage = []
    for line in self.image:
      self.shortImage.append(line[:4])

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

  def display(self):
    print("Player: %s\nMoney: %s\nHand: " % (self.name, self.money))
    self.showHand(True)
    print()

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
    for idx in range(6):
      for i, card in enumerate(self.hand):
        if printShort and i < len(self.hand)-1:
          image = card.shortImage[idx]  if self.knownCards[i] else card.cardBack[idx]
          print(image, end="")
        else:
          image = card.image[idx] if self.knownCards[i] else card.cardBack[idx]
          print(image, end="")
      print()

  def clearHand(self):
    self.hand = []
    self.knownCards = []

  def highest_card(self):
    highest = 0
    result_card = None
    for card in self.hand:
      if(card.value > highest):
        highest = card.value
        result_card = card
    return result_card

  def has_pair(self):
    values = []
    for card in self.hand:
      for value in values:
        if(card.value == value): 
          return True
      values.append(card.value)
    return False

  def bust(self):
    return self.calculateHand() > 21
  
  def showValue(self):
    sum = 0
    for card in self.hand:
      sum += card.value
    return sum

  def printMult(self, players):
    for p in players:
      p.display()

  def calculateHand(self):
    total = self.showValue()
    for card in self.hand:
      if(total < 21):
        break
      if(card.value == 11): # Ace
        total -= 10

    return total


class Dealer:
  def __init__(self, deck: Deck):
    self.deck = deck
    self.deck.shuffle()

  def printCards(self, cards: "list[Player]", showFront: bool, printShort: bool = True):
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

class Pot:
  def __init__(self, money):
    self.money = money

  def addPot(self, amount):
    self.money += amount

  def addPot(self, amount, player):
    if(player.money >= amount):
      self.money += amount
    else:
      print("Error: %s attempted to bet more than they have" % player.name)
    player.makeBet(amount)

  def rewardPot(self, player):
    player.addMoney(self.money)
    self.money = 0

def Play(dealer: Dealer, players: list, pot: Pot):
  #Players make bets after they are dealt their cards
  for player in players:
    player.display()
    current_money = player.money
    bet = 0
    while current_money == player.money and player.money > 0:
      bet = int(input("Place Your Bet!\nAmount: "))
      if bet == 0:
        break
      player.makeBet(bet)
    pot.addPot(bet)
    print("\n")
  
  #Main game loop
  players_passed = []
  while len(players) > 0:
    for player in players:
      player.display()
      draw = input("Enter 'draw' or 'pass': ")
      if draw == "draw" or draw == "Draw":
        dealer.dealCards(1, [player])
        print("Card drawn by %s.\n" % (player.name))
        player.display()
        if player.bust() == True:
          print("You bust!\n")
          players.pop(players.index(player))
      else:
        print("%s passed.\n" % (player.name))
        players_passed.append(player)
        players.pop(players.index(player))
      input("Next Player press 'Enter' when ready!")
  return players_passed

def showWinner(players):
    handTotals = {}
    for player in players:
      handTotals[player.calculateHand()] = player
    winner = handTotals[max(handTotals.keys())] 
    return winner

source_folder = os.path.join(os.getcwd(), '..', 'source')
leaderboard_file = os.path.join(source_folder, 'leaderboard.txt')

def updateLeaderboard(player):
    playerFound = False
    with open(leaderboard_file, 'r') as file:
        lines = file.readlines()
    with open(leaderboard_file, 'w') as file:
        for line in lines:
            if player in line:
                parts = line.split(':')
                winCount = int(parts[1]) + 1
                newLine = f"{parts[0]}:{winCount}\n"
                file.write(newLine)
                playerFound = True
            else:
                file.write(line)
        if not playerFound:
            newLine = f"{player}:1\n"
            file.write(newLine)
  
def showLeaderboard():
    with open(leaderboard_file, 'r') as file:
        leaderboard = file.readlines()
    print('\nLEADERBOARD:')
    for line in leaderboard:
        print(line.strip())
