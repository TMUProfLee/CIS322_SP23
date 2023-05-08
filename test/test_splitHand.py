from testing_base import *

deck = Deck()
deck.shuffle()
dealer = Dealer(deck)
#player_name = Player("User")
#house = Player("house")

five_spades = getCard("spades", 5)

def splitHand(self):
    if self.pairCheck() == True:
        self.showHand()
        split_decision = input("Would you like to split your hand? (y/n) ")
        if split_decision == "y":
            # take both cards and seperatly append them to hands_list
            self.hands_lst.append(self.hand.pop(0))
            self.hands_lst.append(self.hand.pop(0))
            return True
        
class BlackJack:
  
  def blackjackDecider(self, house, player_name, betting_box, dealer, silent: bool=False):
    blackjackOutcome = dealer.blackjackChecker(house, player_name)
    if blackjackOutcome == 1 and silent == False:
      print("The house has blackjack. You lose!")
      print("\nDealer's Hand: ", house.handSum()), house.showHand()
      betting_box.collect(blackjackOutcome)
      print(f"You now have ${player_name.money}")
      return True
    elif blackjackOutcome == 2 and silent == False:
      print("Blackjack! You win!")
      print("\nYour Hand: ", player_name.handSum()), player_name.showHand()
      betting_box.collect(blackjackOutcome)
      print(f"You now have ${player_name.money}")
      return True
    elif blackjackOutcome == 3 and silent == False:
      print("It's a push! You both have blackjack.")
      print("\nYour Hand: ", player_name.handSum()), player_name.showHand()
      print("\nDealer's Hand: ", house.handSum(hideSum=True)), house.showHand(showBack= True)
      betting_box.collect(blackjackOutcome)
      print(f"You now have ${player_name.money}")
      return True
    elif blackjackOutcome == 2:
      print("This hand is blackjack!")
      return True

      
  def restartGame(self, house, player_name, dealer, deck, early_shuffle):
    print("Cards remaining in deck:", deck.size)
    start = input("\nWould you like to play again (y/n)? ")
    if start == "n":
      betting = False
      return betting
    else:
      house.clearHand()
      player_name.clearHand()

class BlackJack:
  
  def blackjackDecider(self, house, player_name, betting_box, dealer, silent: bool=False):
    blackjackOutcome = dealer.blackjackChecker(house, player_name)
    if blackjackOutcome == 1 and silent == False:
      print("The house has blackjack. You lose!")
      print("\nDealer's Hand: ", house.handSum()), house.showHand()
      betting_box.collect(blackjackOutcome)
      print(f"You now have ${player_name.money}")
      return True
    elif blackjackOutcome == 2 and silent == False:
      print("Blackjack! You win!")
      print("\nYour Hand: ", player_name.handSum()), player_name.showHand()
      betting_box.collect(blackjackOutcome)
      print(f"You now have ${player_name.money}")
      return True
    elif blackjackOutcome == 3 and silent == False:
      print("It's a push! You both have blackjack.")
      print("\nYour Hand: ", player_name.handSum()), player_name.showHand()
      print("\nDealer's Hand: ", house.handSum(hideSum=True)), house.showHand(showBack= True)
      betting_box.collect(blackjackOutcome)
      print(f"You now have ${player_name.money}")
      return True
    elif blackjackOutcome == 2:
      print("This hand is blackjack!")
      return True

  def restartGame(self, house, player_name, dealer, deck, early_shuffle):
    print("Cards remaining in deck:", deck.size)
    start = input("\nWould you like to play again (y/n)? ")
    if start == "n":
      betting = False
      return betting
    else:
      house.clearHand()
      player_name.clearHand()

    if deck.size <=52 and early_shuffle:
      dealer.resetDeck()

  def winnerCompare(self, house, player_name, dealer, betting_box):
    #print("\n")
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

  def houseTurn(self, house, dealer):
    dealer.dealerHand(house)
    print("\nDealer's Hand: ", house.handSum())
    if dealer.bustCheck(house) == True:
      print("\nThe Dealer Bust!")
      house.showHand()
    else:
      house.showHand()

  def playerTurn(self, player_name, dealer):
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

  def print_startingHands(self, house, player_name):
    print("\nYour Hand: ", player_name.handSum()), player_name.showHand()
    print("\nDealer's Hand: ", house.handSum(hideSum=True)), house.showHand(showBack= True)

  def playerBet(self, player_name, for_money):
    if for_money:
      """Player Bet"""
      if player_name.money == 0:
        print("You lost all your money gambeling ;( . . . . Come back later when you get more! :)")
        return "no money"
      bet = int(input("How much would you like to bet? "))
      while bet == 0:
        print("You must bet something!")
        bet = int(input("How much would you like to bet? "))
      while player_name.makeBet(bet) == False:
        bet = int(input("\nHow much would you like to bet? "))
    else:
      bet=0
    return bet
  
  def configSettings(self, player_name):
    deck_num = 1
    for_money = True
    early_shuffle = False

    partition = player_name.find(";")
    config=""
    if partition > 0:
      config = player_name[partition:]
      player_name = player_name[0:partition]

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

    return for_money, deck_num, early_shuffle, player_name
  
  def messageBetweenHands(self, player_name):
      if len(player_name.hands_lst) > 0:
        playerORdealer = "your next"
      else:
        playerORdealer = "the dealer's"
        
      phrase = (f"Getting {playerORdealer} hand")

      for letter in phrase:
        print(letter, end="", flush=True), time.sleep(.01)

      for dash in range(10):
        print(" .",end="", flush=True), time.sleep(.1)
      print()
#####################################################################################################################
"""Pygame Initializations"""
import pygame 
  
pygame.init() 
  
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
#####################################################################################################################
def blackjackGame():
  """Pygame initialization"""
  screen.fill((60,25,60))
  pygame.display.update()
  """blackjack Class initialization"""
  bj = BlackJack()

  """Get Player_name"""
  player_name = input("Enter Username: ")

  """player config settings and Deck, dealer initializations"""
  for_money, deck_num, early_shuffle, player_name = bj.configSettings(player_name)
  deck = Deck(deck_num)
  deck.shuffle()
  dealer = Dealer(deck)

  """Player Class initializations"""
  player_name = Player(player_name)
  player_name.addMoney(500)
  house = Player("house")

  ####"""Game Loop"""####
  betting = True
  while betting:

    hand_num = 1 # at the top of the loop, we are always looking at hand number 1

    """This catches and disrupts the normal game loop if the player is in the middle of playing their split hands"""
    while len(player_name.hands_lst) > 0:
      current_hand = []
      current_hand.append(player_name.hands_lst.pop(0))
      player_name.hand = current_hand # rotating which hand to look at from the hands_lst
      dealer.dealCards(1, [player_name])
      print("Hand "+ str(hand_num) + " sum:", player_name.handSum())
      player_name.showHand()

      """Checks if the hand is blackjack. If not, then allow the player to complete the turn for that hand"""
      if bj.blackjackDecider(house, player_name, betting_box, dealer, silent=True) == True:
        player_name.completed_hands.append(player_name.hand)
      else:
        bj.playerTurn(player_name, dealer)
        player_name.completed_hands.append(player_name.hand)
      
      """distinguish which hand is being looked at and slow down gameplay"""
      bj.messageBetweenHands(player_name)
      hand_num += 1 # keeps track of what hand is being looked at

    """After the player is done, let the house complete its turn"""
    if len(player_name.completed_hands) > 0:
        bj.houseTurn(house, dealer)

        """Compare house and player's hands to see who wins. Then handle win/loss interaction."""
        hand_num = 1
        for hand in player_name.completed_hands:
          print(f"\nComparing hand {hand_num} against the house")
          player_name.hand = hand
          bj.winnerCompare(house, player_name, dealer, betting_box)
          hand_num += 1

        """After all hands have been compared with the house, clear the completed_hands list"""
        player_name.completed_hands = []

        """After all the hands have been gone through, ask if they want to play again"""
        if bj.restartGame(house, player_name, dealer, deck, early_shuffle) == False:
          break
    ###NORMAL GAMELOOP####
    else:
      """handle Player betting"""
      bet = bj.playerBet(player_name, for_money)
      if bet == "no money":
        break 
      else:
        betting_box = Betting_box(bet, [player_name])
                
      """Give both the house and the player 2 cards to start the game"""
      dealer.dealCards(2, [player_name, house])
      
      """check to see if someone has blackjack"""
      if bj.blackjackDecider(house, player_name, betting_box, dealer) == True:
        pass

      else:
        """check to see if player can and wants to split their hand"""
        if player_name.splitHand() == True:
          pass # if they do, pass on normal game loop
        else:
        
          """Print both hands of the player and dealer"""
          bj.print_startingHands(house, player_name)

          """while the player doesn't bust, allow them to choose to hit or pass"""
          bj.playerTurn(player_name, dealer)

          """After the player is done, let the house complete its turn"""
          bj.houseTurn(house, dealer)
          
          """Compare house and player's hands to see who wins. Then handle win/loss interaction."""
          bj.winnerCompare(house, player_name, dealer, betting_box)

          """Clear hands and ask if they want to play again"""
      if len(player_name.hands_lst) == 0: # if you aren't in the middle of playing your split hands then give the option to quit or continue
        if bj.restartGame(house, player_name, dealer, deck, early_shuffle) == False:
          break

blackjackGame()
