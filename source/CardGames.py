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

  def count_cards(deck):  #How many cards are in the deck assigned to "num_cards"  
    num_cards = deck.size()
    #For each iteration the number of cars in the deck decrease by 1 card  
    for i in range(num_cards):    
      print("There are "+ str(num_cards - i) +" more cards in the deck")
      #when the deck reaches 0, then the game is over  
      if num_cards == 0:      
        print("The deck is now empty. Game over, Thanks for playing!")  
  
####################################################################################
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
    print("There are "+ str(num_cards) +" more cards in the deck")
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
  def __init__(self):
    self.playerinfo = []
    self.players = []
    self.player_dict = {}
    self.value_wanted = 0
    self.player_asked = None
    self.player_turn = None
    self.info_player_turn = 0
    self.info_player_asked = 0
    self.deck = Deck()
    self.dealer = Dealer(self.deck)
    self.width = os.get_terminal_size().columns

  def start_game(self):
    
    print("*._."*(self.width//4))
    print()
    print("Welcome to Go Fish!".center(self.width))
    print()
    print("*._."*(self.width//4))

    player_number = self.multiplayer_info()
    self.point_tracker_interface(player_number)

    
    self.dealer.dealCards(5, self.players)
    for player in self.players:
      print("\n",player)
      player.showHand(player.hand)

    self.game_loop()

  def game_loop(self):
      repeat = True
      while self.count_cards() != True:
          for key in self.players:
            turn_repeat = self.ask_card(key)
            while turn_repeat == "go_again":
              turn_repeat = self.ask_card(key)

              print()

  def ask_card(self, player_turn):
    width = os.get_terminal_size().columns
    deco = "*-"*(width//2)

    self.player_deck_info()
    
    
    print(deco)
    print()

    print(("%s it's your turn!" %player_turn).center(width))
    player_asked = input("%s who would like to ask? " % str(player_turn))

    print()
   
    self.value_wanted = int(input("What value would you like? "))
    self.info_player_turn = self.playerinfo[self.index(player_turn, self.playerinfo)][1]
    self.info_player_asked = self.playerinfo[self.index(player_asked, self.playerinfo)][1]
    self.player_turn = self.playerinfo[self.index(player_turn, self.playerinfo)][0]
    self.player_asked = self.playerinfo[self.index(player_asked, self.playerinfo)][0]
    turn_value = self.sayGoFish()
      
    self.surrender_card()

    return turn_value
    
  def confirm_value(self):
    confirm_value = True
    while confirm_value:
      confirm = input("is this correct? Y/N: ")
      if confirm == "n":
        num_players = int(input("How many players? "))
      elif confirm == "y":
        confirm_value = False
      else:
        print("\n[Please input Y/N]\n")
          
  def multiplayer_info(self):
    width = os.get_terminal_size().columns
    print()
    print("*-"*(width//2))
  
    num_players = int(input("How many players? "))

    print()

    print("%d players selected" %num_players, "\n")

    self.confirm_value()
        
    for i in range(1, num_players+1):
      print()
      player = input("Player %d What is your name? " %i)
      self.players.append(Player(player))

    print()
    print("*-"*(width//2))
    print("[ TOTAL NUMBER OF PLAYERS ]".center(width))
    print(str(num_players).center(width))

    return self.assign_player_numbers()

  def assign_player_numbers(self):
    player_num = {}

    youngest_player = self.playerages()
    self.players.insert(0, self.players.pop(self.players.index(youngest_player)))

    for counter, player in enumerate((self.players), start =1):
      print("PLAYER %d: " % counter, player)
      player_num[counter] = player
    print()
    self.player_dict = player_num
    return player_num
      
  def point_tracker_interface(self, info):
    width = os.get_terminal_size().columns
    score = 0

    print("*-"*(width//2))
    
    print("[ PLAYER SCORES ]".center(width))
    for num, player in info.items():
      print(("{0}: {1}".center(width)).format(player, score))

    print()
    print("*-"*(width//2))


  def count_cards(self):  #How many cards are in the deck assigned to "num_cards"  
      num_cards = self.deck.size
      print()
      print(" "*25, "*"*5)
      print("cards remaining in deck: ", num_cards)
      print(" "*25, "*"*5)
      print()
      #For each iteration the number of cars in the deck decrease by 1 card  
      if num_cards == 0:
        print("The deck is now empty. Game over, Thanks for playing!")
        self.game_over()
        return True



  def game_over(self):
    width = os.get_terminal_size().columns
    deco = "*-"*(width//2)
    j = 0
    gm = ["G", "A", "M", "E", "O", "V", "E","R"]
    print(deco)
    for i in range(width//8):
      print("  "*j, ". *")
      j += 3
      if i == 10:
        for i in range (len(gm)):
          print("  "*j, gm[i])
          j += 3
    print(deco)
    sys.exit()


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
    counter = 0
    self.count_cards()
    if len(self.info_player_asked) == 0:
          self.game_over()

    for i in self.info_player_asked:
      if str(i) != str(self.value_wanted):
        counter += 1 
      else:
        temp_list1.append(self.info_player_asked[counter])
        counter += 1 

    if len(temp_list1) != 0:
      for card in temp_list1:
        self.player_turn.addCard(card)
        self.info_player_asked.remove(card)
        

    for player in self.players:
      print(str(player))
      player.showHand()
      print()


  def sayGoFish(self):   
    width = os.get_terminal_size().columns
    print()
    deco = "*-"*(width//2)
    response = input("Do you have any of the requested cards? (YES/NO): ")      
    if response.upper() == "NO": 
      self.player_turn.addCard(self.deck.getCard())
            
      print()
      return print("GO FISH!!".center(width), deco)
      
    elif response.upper() == "YES":          
      return "go_again"
    else:          
      return "Looks like there was a typo in your response, please try again"
#self.surrender_card()

  def playerages(self):
      playerAge = []
      for player in self.players:
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
      return youngestPlayer

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