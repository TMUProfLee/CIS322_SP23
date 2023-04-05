
import random
import os
import time
import itertools

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
    if self.image:
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

  def drawCard(self):
      """
      Draw a card from the top of the deck.
      Returns:
        Card: The card drawn from the top of the deck.
      """
      if self.size > 0:
        card = self.getCard()
        print(f"Card drawn: {card.suit} {card.value}")
        return card
      else:
        print("No cards left in the deck.")
        return None

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
#when the deck reaches 0, then the game is over
  if num_cards == 0:
      print("The deck is now empty. Game over, Thanks for playing!")
#####################################################################################
class Player:
  def __init__(self, name, money: int = 0):
    self.name = name
    self.hand = []
    self.knownCards = []
    self.money = money
    
  def __str__(self):
    return (str(self.name))
    self.setsOfFour = {}

  def addSetOfFour(self, value: int):
    if value in self.setsOfFour:
      self.setsOfFour[value] += 1
    else:
      self.setsOfFour[value] = 1

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
    for combination in itertools.combinations(self.hand, 4):
      if all(card.value == combination[0].value for card in combination):
        print("You have a set of %ss!" % combination[0].value)
        self.addSetOfFour(combination[0].value)
        return True
    return False

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

  def printHand(self):
    list1 = []
    for i in self.hand:
      list1.append(str(i))
    return list(map(int, list1))

  def get_playerHand(self):
    print()

  def addValues(self):
    list1 = []
    for i in self.hand:
      list1.append(str(i))
    integer_list = list(map(int, list1))
    return sum(integer_list)
  
  def printCardsIfSet(self):
    # Check for a set of four cards with the same value
    value_counts = {}
    for card in self.hand:
      if card.value not in value_counts:
        value_counts[card.value] = 1
      else:
        value_counts[card.value] += 1
      if value_counts[card.value] == 4:
        print("You have a set of four %s's!" % card.value)
        print("Would you like to print your hand? (Y/N)")
        choice = input().lower()
        if choice == 'y':
          self.showHand()
        return

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
  

  def printHands(self, players: dict):
    # Show each player's hand
    for player in players.values():
        print(f'{player.name}:')
        player.showHand(True)
        print() 
class GoFish:
  def __init__(self):
    self.playerinfo = []
    self.players = []
    self.value_wanted = int
    self.suit_wanted = ""
    self.player_asked = ""
    self.player_turn = ""
    self.info_player_turn = int
    self.info_player_asked = int

  def multiplayer_info(self):
    #for print statements and centering
    width = os.get_terminal_size().columns
    confirm_value = True

    print()
    print("*-"*(width//2))

    #ask total num players
    player_num = {}
    num_players = int(input("How many players? "))
    print()
    print("%d players selected" %num_players, "\n")

    #confirm input 
    while confirm_value:
      confirm = input("is this correct? Y/N: ")

      if confirm == "n":
        num_players = int(input("How many players? "))

      elif confirm == "y":
        confirm_value = False

      else:
        #if user chooses anything other than Y?N
        print("\n[Please input Y/N]\n")
        
    #makes player object with their name
    for i in range(1, num_players+1):
      print()
      player = input("Player %d What is your name? " %i)
      self.players.append(Player(player))

    print()
    print("*-"*(width//2))
    print("[ TOTAL NUMBER OF PLAYERS ]".center(width))
    print(str(num_players).center(width))

    #adds number, player to dictionary (ex: 1, Keren) 
    #Keren is player 1 
    for counter, player in enumerate((self.players), start =1):
      print("PLAYER %d: " % counter, player)
      player_num[counter] = player
    print()
    return player_num
      
  #player score will be shown here
  def point_tracker_interface(self, info):
    width = os.get_terminal_size().columns
    score = 0

    print("*-"*(width//2))
    
    print("[ PLAYER SCORES ]".center(width))
    for num, player in info.items():
      print(("{0}: {1}".center(width)).format(player, score))

    print()
    print("*-"*(width//2))



  def start_game(self):
    player_number = self.multiplayer_info()
    self.point_tracker_interface(player_number)

    deck = Deck()
    dealer = Dealer(deck)
    dealer.dealCards(5, self.players)
    for player in self.players:
      print("\n",player)
      player.showHand(player.hand)

  def check_if_empty(self):
    if len(self.info_player_asked) == 0:
          self.game_over()

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
    temp_list2 = []
    counter = 0

    self.check_if_empty()

    for i in self.info_player_asked:
      if str(i) != str(self.value_wanted):
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

        del self.info_player_asked[counter]
        self.check_if_empty()

    print("\n", self.player_turn)
    self.player_turn.showHand()
    print("\n", self.player_asked)
    self.player_asked.showHand()

  def ask_card(self):
    self.player_deck_info()
    player_turn = input(str("What is your name? "))
    player_asked = input(str("Who would like to ask? "))

    self.value_wanted = int(input("What value would you like? "))
    self.suit_wanted = str(input("What suit would you like? "))

    self.info_player_turn = self.playerinfo[self.index(player_turn, self.playerinfo)][1]
    self.info_player_asked = self.playerinfo[self.index(player_asked, self.playerinfo)][1]

    self.check_if_empty()

    self.value_wanted = int(input("What value would you like? "))
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

def player_ages(players):
    playerAge = []
    for player in players.values():
        while True:
            try:
                age = int(input("Enter {}'s age: ".format(player.name)))
                playerAge.append((player, age))
                break
            except ValueError:
                print("Please enter a valid age: ")
    playerAge = sorted(playerAge, key=lambda x: x[1])
    youngestPlayer = playerAge[0][0]
    print("{} goes first!\n".format(youngestPlayer.name))
    return [p for p, _ in playerAge]

def playerTurn(players: list, current_player: str, getCard: bool) -> None:
  """Determines which player's turn it is

  Args:
      players (list): list of players in order
      current_player (str): name of current player
      getCard (bool): received card from deck

  Returns:
      None
  """
  num_players = len(players)
  if getCard == False:
      return current_player
  else:
      next_player_index = (players.index(current_player) + 1) % num_players
      next_player = players[next_player_index]
      return next_player

def endScreen(players):
    import tkinter as tk
    #Create window and greeting 
    window = tk.Tk()
    window.geometry("500x500")
    greeting = tk.Label(text="Good Game! Here's the results:")
    greeting.configure(font=("Calibri", 30), fg="green")
    greeting.pack(pady=50)
    #Create list of players and scores
    player_list = tk.Listbox(window, width=50, font=("Calibri", 24), fg="gold")
    player_list.pack(pady=20)

    sorted_players = sorted(players.items(), key=lambda x: x[1], reverse=True)

    for player, score in sorted_players:
        player_list.insert(tk.END, f"{player}: {score}")

    window.mainloop()
