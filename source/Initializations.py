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