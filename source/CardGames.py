import random
import os
import pygame 
pygame.init() 

cardImages = []
values = [11,2,3,4,5,6,7,8,9,10,10,10,10] # blackjack card values
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

#pygame surfaces can be blit onto screen
cardback = pygame.image.load("source/Cards/redBack.png")
cardSurfaceList =[]

#spades
cardSurfaceList .append( pygame.image.load("source/Cards/ace_spades.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/two_spades.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/three_spades.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/four_spades.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/five_spades.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/six_spades.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/seven_spades.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/eight_spades.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/nine_spades.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/ten_spades.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/jack_spades.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/queen_spades.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/king_spades.png"))

#clubs
cardSurfaceList .append( pygame.image.load("source/Cards/ace.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/two.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/three.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/four.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/five.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/six.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/seven.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/eight.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/nine.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/ten.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/jack.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/queen.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/king.png"))

#hearts
cardSurfaceList .append( pygame.image.load("source/Cards/ace_heart.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/two_heart.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/three_heart.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/four_heart.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/five_heart.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/six_heart.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/seven_heart.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/eight_heart.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/nine_heart.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/ten_heart.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/jack_heart.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/queen_heart.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/king_heart.png"))

#diamonds
cardSurfaceList .append( pygame.image.load("source/Cards/ace_diamond.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/two_diamond.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/three_diamond.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/four_diamond.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/five_diamond.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/six_diamond.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/seven_diamond.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/eight_diamond.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/nine_diamond.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/ten_diamond.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/jack_diamond.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/queen_diamond.png"))
cardSurfaceList .append( pygame.image.load("source/Cards/king_diamond.png"))


def find_root_dir():
  cwd = os.getcwd()
  while 'source' not in os.listdir():
    os.chdir('..')
    cwd = os.path.join( cwd, '..')
  return cwd
######################################################################################################################
class Card:
  def __init__(self, suit, value, image, cardBack,surfaceObj=None):
    self.cardBack = cardBack
    self.suit = suit
    self.value = value
    self.image = image
    self.shortImage = []
    self.surfaceObj = surfaceObj
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
  def __init__(self,cardSurfaceList,deck_count=1):#by default the number of deck is one
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
          deck.append(Card(suit, value, cardImages[index], cardBack,cardSurfaceList[index]))
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
  def cardImages(self):#returns a list of surface objects
    aList =[]
    for card in self.hand:
      aList.append(card.surfaceObj)
    return aList
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

def wait():
  waiting = False
  while not waiting:#makes certain the user has let go of the button
    for event in pygame.event.get():
      if event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP:
        waiting = True
        pygame.event.clear()
  while waiting:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
            
      if event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP:
        waiting = False
def handsDisplay(hidden=True):
    #house cards
    if not hidden:
      x= 505 - 45*len(house.cardImages())
      for acard in house.cardImages():
        screen.blit(acard,(x,120))
        x+=90
    if hidden:
      screen.blit(cardback,(500,120))
      screen.blit(house.cardImages()[0],(400,120))
    #player cards
    x= 505 - 45*len(player_name.cardImages())
    for acard in player_name.cardImages():
      screen.blit(acard,(x,420))
      x+=90
#####################################################################################################################
"""Initializations"""
  
# screen size
res = (1080,720) 
  
# opens up a window 
screen = pygame.display.set_mode(res) 
  

color = (255,255,255) 
color_light = (170,170,170) 
color_dark = (100,100,100) 
  
width = screen.get_width() 
height = screen.get_height() 

#options
deck_num = 1
early_shuffle = False
for_money=True#unused


##menu

smallfont = pygame.font.SysFont('Corbel',35)

#to add a new button only lines marked with ~~~ must be added
quit_text = smallfont.render('QUIT' , True , color) #   ~~~
decks_text = smallfont.render('decks' , True , color)
play_text = smallfont.render('PLAY' , True , color)
early_text = smallfont.render('shuffle' , True , color)

buttonlist=[        #[left,up,width,hight,text_offset]
    [   [480,500,120,35,20],quit_text ],#   ~~~
    [   [480,350,120,35,20],decks_text ],
    [   [480,100,120,35,20],play_text ],
    [   [480,200,120,35,10],early_text ]
]


in_menu=True 
while in_menu: 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            element = buttonlist[0]#first button   ~~~
            if element[0][0] <= mouse[0] <= element[0][0]+element[0][2] and element[0][1] <= mouse[1] <= element[0][1]+element[0][3]:#   ~~~ 
                pygame.quit()#   ~~~

            element = buttonlist[1]#second button
            if element[0][0] <= mouse[0] <= element[0][0]+element[0][2] and element[0][1] <= mouse[1] <= element[0][1]+element[0][3]: 
                if deck_num==1:
                    deck_num=2
                elif deck_num==2:
                    deck_num=4
                elif deck_num==4:
                    deck_num=8
                elif deck_num==8:
                    deck_num=1

            element = buttonlist[2]#third button
            if element[0][0] <= mouse[0] <= element[0][0]+element[0][2] and element[0][1] <= mouse[1] <= element[0][1]+element[0][3]:
                in_menu=False
            
            element = buttonlist[3]#fouth button
            if element[0][0] <= mouse[0] <= element[0][0]+element[0][2] and element[0][1] <= mouse[1] <= element[0][1]+element[0][3]:
                if not early_shuffle:
                    early_shuffle = True
                else:
                  early_shuffle = False

    # background color 
    screen.fill((60,25,60)) 
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
      
    # if mouse is hovered on a button it changes to a lighter shade 
    for element in buttonlist:
        if element[0][0] <= mouse[0] <= element[0][0]+element[0][2] and element[0][1] <= mouse[1] <= element[0][1]+element[0][3]: 
            pygame.draw.rect(screen,color_light,[element[0][0],element[0][1],element[0][2],element[0][3]]) 
          
        else: 
            pygame.draw.rect(screen,color_dark,[element[0][0],element[0][1],element[0][2],element[0][3]]) 
      
        # superimposing the prompt text onto our button 
        screen.blit(element[1], (element[0][0]+element[0][4],element[0][1])) 

    #button values displayed

    #deck value
    deckCount = smallfont.render( str(deck_num), True , color)
    element = buttonlist[1]#second button
    screen.blit(deckCount, (element[0][0]+element[0][4]+30,element[0][1]+40))
    #shuffle style
    if early_shuffle:
        indeck_limit=52*deck_num//2
    else:
        indeck_limit=0
    earlyValue = smallfont.render( "at: "+str(indeck_limit), True , color)
    element = buttonlist[3]#fouth button
    screen.blit(earlyValue, (element[0][0]+element[0][4]+10,element[0][1]+40))

    pygame.display.update() 

##game
background=(0,60,60)
screen.fill((background))
pygame.display.update()
player_name = "john"

deck = Deck(cardSurfaceList,deck_num)
deck.shuffle

dealer = Dealer(deck)
player_name = Player(player_name)
player_name.addMoney(500)
house = Player("house")


promptText = smallfont.render( "Press/Click to continue.", True , color)
betting = True
while betting:

    """Player Bet"""
    if player_name.money == 0:
        "You lost all your money gambeling ;( . . . . Come back later when you get more! :)"
        break

    wager="0"
    asking_for_bet =True
    while asking_for_bet:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
              if len(wager)>0 and wager != "0":
                wager = wager[:-1]
              if wager == "":
                wager = "0"
            elif event.key == pygame.K_RETURN:
              if int(wager) <= player_name.money:
                asking_for_bet = False
            elif event.unicode.isdigit() :
              if wager == "0":
                wager = wager[:-1]
              wager += event.unicode


        screen.fill((background))
        wager_text = smallfont.render( "wager: "+wager, True , color)
        screen.blit(wager_text, (400,360))
        walletText = smallfont.render("reserve: $"+str(player_name.money),True, color)
        screen.blit(walletText, (12,6))
        pygame.display.update()

    bet = int(wager)
    player_name.makeBet(bet)
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

      screen.fill((background))
      handsDisplay(False)#blits the cards to the screen
      lwp = smallfont.render( "The house has blackjack. You lose!", True , color)
      screen.blit(lwp, (300,320))
      screen.blit(promptText, (350,385))
      walletText = smallfont.render("reserve: $"+str(player_name.money),True, color)
      screen.blit(walletText, (12,6))
      pygame.display.update()
      wait()

    elif blackjackOutcome == 2:
      print("Blackjack! You win!")
      betting_box.collect(blackjackOutcome)
      print(f"You now have ${player_name.money}")

      screen.fill((background))
      handsDisplay(False)#blits the cards to the screen
      lwp = smallfont.render( "Blackjack! You win!", True , color)
      screen.blit(lwp, (340,320))
      screen.blit(promptText, (350,385))
      walletText = smallfont.render("reserve: $"+str(player_name.money),True, color)
      screen.blit(walletText, (12,6))
      pygame.display.update()
      wait()

    elif blackjackOutcome == 3:
      print("It's a push! You both have blackjack.")
      betting_box.collect(blackjackOutcome)
      print(f"You now have ${player_name.money}")
      
      screen.fill((background))
      handsDisplay(False)#blits the cards to the screen
      lwp = smallfont.render( "It's a push! You both have blackjack.", True , color)
      screen.blit(lwp, (240,320))
      screen.blit(promptText, (350,385))
      walletText = smallfont.render("reserve: $"+str(player_name.money),True, color)
      screen.blit(walletText, (12,6))
      pygame.display.update()
      wait()

    else:
      """while the player doesn't bust, allow them to choose to hit or pass"""
      bust = False
      while not bust :
        screen.fill((background))
        playPrompt = smallfont.render( 'Press "h" to hit and "s" to stand', True , color)
        screen.blit(playPrompt, (200,320))  
        handsDisplay()#blits the cards to the screen
        walletText = smallfont.render("reserve: $"+str(player_name.money),True, color)
        screen.blit(walletText, (12,6))
        pygame.display.update()
        
        hit_stand = ""
        while hit_stand =="":
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()

            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_h or event.key == pygame.K_j or event.key == pygame.K_k or event.key == pygame.K_l:
                hit_stand = "hit"
              if event.key == pygame.K_f or event.key == pygame.K_d or event.key == pygame.K_s or event.key == pygame.K_a:
                hit_stand ="stand"

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

        screen.fill((background))
        handsDisplay(False)#blits the cards to the screen
        resultText = smallfont.render( "You won!", True , color)
        screen.blit(resultText, (320,300))
        screen.blit(promptText, (320,350))
        walletText = smallfont.render("reserve: $"+str(player_name.money),True, color)
        screen.blit(walletText, (12,6))
        pygame.display.update()
        wait()
      elif winner == 1:
        print("You lost. The dealer won!")
        betting_box.collect(winner)
        print(f"You now have ${player_name.money}")

        screen.fill((background))
        handsDisplay(False)#blits the cards to the screen
        resultText = smallfont.render( "You lost!", True , color)
        screen.blit(resultText, (320,300))
        screen.blit(promptText, (320,350))
        walletText = smallfont.render("reserve: $"+str(player_name.money),True, color)
        screen.blit(walletText, (12,6))
        pygame.display.update()
        wait()
      else:
        print("It's a push!")
        betting_box.collect(winner)
        print(f"You now have ${player_name.money}")

        screen.fill((background))
        handsDisplay(False)#blits the cards to the screen
        resultText = smallfont.render( "It's a push!", True , color)
        screen.blit(resultText, (320,300))
        screen.blit(promptText, (320,350))
        walletText = smallfont.render("reserve: $"+str(player_name.money),True, color)
        screen.blit(walletText, (12,6))
        pygame.display.update()
        wait()

    """"Clear hands"""
    print("Cards remaining in deck:", deck.size)


    house.clearHand()
    player_name.clearHand()

    if deck.size <=52*deck_num//2 and early_shuffle:
      dealer.resetDeck()