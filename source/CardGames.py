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
######################################################################################################################
class Card:
  def __init__(self, suit, value, image, cardBack):
    self.cardBack = cardBack
    self.suit = suit
    self.value = value
    self.image = image
    self.shortImage = []
    if self.image:
      for line in self.image:
        self.shortImage.append(line[:4])

  def __eq__(self, other):
    if not type(other) == Card:
      return False
    return self.suit == other.suit and \
      self.value == other.value
#######################################################################################################################
class Deck:
  def __init__(self,deck_count=1):#by default the number of deck is one
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
    while deck_count > 0:
      index = 0
      for suit in suits:
        for value in values:
          deck.append(Card(suit, value, cardImages[index], cardBack))
          index += 1
      deck_count -= 1
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
#######################################################################################################################
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
####################################################################################################################
class Player:
  def __init__(self, name, money: int = 0):
    self.name = name
    self.hand = []
    self.knownCards = []
    self.money = int(money)
  
  def display(self):
    print("Name: " + self.name + "|| Money: " + str(self.money) + "|| Hand: " + str(self.handSum()))
    self.showHand(False)

  def addMoney(self, amount: int):
    self.money += amount
    return self.money

  def makeBet(self, amount: int):
    if amount > self.money:
      print(f"{self.name} has {self.money} dollars. This is not enough to make this bet.")
      return False
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
        #If the cardvalue is already in the pairlist, take note and set duplicate check to True
        for cardValue in pairlist:
          if cardValue == self.hand[aVar1].value:
            duplicateCheck = True
        #If the cardvalues match and are not already in the parilist then add them
        if self.hand[aVar1].value == self.hand[aVar2].value and not duplicateCheck :
          pairlist.append(self.hand[aVar1].value)
        aVar2 += 1
      aVar1 += 1
    return(pairlist)

  def matching(self):# returns a list of cards and the amount of pairs of each card in the player's hand
    report = []
    pairlist = self.pairCheck()
    for pairValue in pairlist:
      matches = 0
      for aCard in self.hand:
        if aCard.value == pairValue:
          matches += 1
      # Checks to see if the card has a match, if not then disregard the card without a match
      if matches % 2 != 0:
        matches -= 1
      report.append([pairValue,matches/2])
    return report
  
  def clearHand(self):
    self.hand = []
    self.knownCards = []
##################################################################################################################
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
      self.resetDeck()
    for player in players:
      for _ in range(numCards):
        player.addCard(self.deck.getCard())
    return True

  def resetDeck(self):
    self.deck.reset()
    self.deck.shuffle()

  def blackjackChecker(self, house, player):
    houseHand = house.handSum()
    playerHand = player.handSum()
    player_outcome = 0
    house_outcome = 0
    if playerHand == 21 and len(player.hand) == 2: #if the player has blackjack then set their outcome to be the inverse of the house
      player_outcome = 2   
    if houseHand == 21 and len(house.hand) == 2: #if the house has blackjack then set their outcome to be the inverse of the player
      house_outcome = 1 
    outcome = player_outcome + house_outcome
    if outcome == 0:
      return 0
    elif outcome == 3:
      return 3
    elif outcome == 2:
      return 2
    else:
      return 1
    
  # simple respond for dealer in single player with known hands 
  def dealerHand(self, house):
    houseHand = house.handSum()
    
    while houseHand < 17: #force hit when below 17
      dealer.dealCards(1, [house])
      houseHand = house.handSum()
    
  def bustCheck(self, player):
    if player.handSum() > 21:
        return True
  
  def winnnerCheck(self, house, player):
    houseHand = house.handSum()
    playerHand = player.handSum()

    if playerHand == houseHand and playerHand <= 21:
      return -1
    
    elif playerHand > 21 and houseHand > 21:
      return 0
    
    elif playerHand > houseHand:
      return 1 if playerHand > 21 else 2
    
    else:
      return 1 if houseHand <= 21 else 2
#####################################################################################################################
"""Initializations"""

player_name = input("Username: ")

partition = player_name.find(";")
config=""
if partition > 0:
  config = player_name[partition:]
  player_name = player_name[0:partition]
###
deck_num = 1
for_money = True
early_shuffle = False
###
i=0
label = ""
while i < len(config):
  if config[i] == ";":
    label =""
  else:
    label = label + config[i]
  i += 1
  
  if label == "free":
    for_money = False
  if label == "four":
    deck_num = 4
  if label == "shuffle":
    early_shuffle = True

deck = Deck(deck_num)
deck.shuffle

dealer = Dealer(deck)
player_name = Player(player_name)
player_name.addMoney(500)
house = Player("house")

betting = True

while betting:
    
    if for_money:
      """Player Bet"""
      if player_name.money == 0:
        "You lost all your money gambeling ;( . . . . Come back later when you get more! :)"
        break
      bet = int(input("How much would you like to bet? "))
      while player_name.makeBet(bet) == False:
        bet = int(input("\nHow much would you like to bet? "))
    else:
      bet=0
  
    betting_box = Betting_box(bet, [player_name])

    """Give both the house and the player 2 cards to start the game"""
    dealer.dealCards(2, [player_name, house])
    print("\nYour Hand: ", player_name.handSum())  
    player_name.showHand()
    print("\nDealer's Hand: ", house.handSum())
    house.showHand()

    """check to see if someone has blackjack"""
    blackjackOutcome = dealer.blackjackChecker(house, player_name)
    if blackjackOutcome == 1:
      print("The house has blackjack. You lose!")
      betting_box.collect(blackjackOutcome)
      print(f"You now have ${player_name.money}")
    elif blackjackOutcome == 2:
      print("Blackjack! You win!")
      betting_box.collect(blackjackOutcome)
      print(f"You now have ${player_name.money}")
    elif blackjackOutcome == 3:
      print("It's a push! You both have blackjack.")
      betting_box.collect(blackjackOutcome)
      print(f"You now have ${player_name.money}")
      
    else:
      """while the player doesn't bust, allow them to choose to hit or pass"""
      bust = False
      while not bust :
        hit_stand = input("\nhit or stand? ")
        if hit_stand == "hit":
          dealer.dealCards(1,[player_name])
          print("\nYour Hand: ", player_name.handSum())  
          player_name.showHand()
          if dealer.bustCheck(player_name) == True:
            print("\nBust!")
            bust = True
        else:
          break
      
      """After the player is done, let the house complete its turn"""
      handChangeDetector = house.handSum()
      dealer.dealerHand(house)
      print("\nDealer's Hand: ", house.handSum())
      if dealer.bustCheck(house) == True:
        print("\nBust!")
      if house.handSum() == handChangeDetector:
        pass
      else:
        house.showHand()
      
      """Compare house and player's hands to see who wins. Then handle win/loss interaction."""
      print("\n")
      winner = dealer.winnnerCheck(house, player_name)
      if winner == 2:
        print("You won!")
        betting_box.collect(winner)
        print(f"You now have ${player_name.money}")
      elif winner == 1:
        print("You lost. The dealer won!")
        betting_box.collect(winner)
        print(f"You now have ${player_name.money}")
      else:
        print("It's a push!")
        betting_box.collect(winner)
        print(f"You now have ${player_name.money}")

    """"Clear hands and ask if they want to play again"""
    print("Cards remaining in deck:", deck.size)
    start = input("\nWould you like to play again (y/n)? ")
    if start == "n":
      betting = False
    else:
      house.clearHand()
      player_name.clearHand()

    if deck.size <=52 and early_shuffle:
      dealer.resetDeck()