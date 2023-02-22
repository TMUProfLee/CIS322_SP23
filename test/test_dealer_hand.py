from testing_base import *

# Create a deck to use
deck = Deck()
# Create a dealer
dealer = Dealer(deck)
# Create players for your game
player = Player('Matthew')
house = Player('House')
#Dealer gets 2 cards
dealer.dealCards(2, [house])
#all case where player win
def test_player_win():
    # Case1: Player get BlackJack hand fist
    # player: 21 and 2 cards only
    firstCard = getCard("Spades", 10)
    secondCard = getCard("Spades", 11)
    cards = [ firstCard, secondCard]
    player.setHand( cards, isKnown=True )
    house.setHand( cards, isKnown=True )
    assert dealerHand(dealer, house, player) == 1
    # case 2: House get over 21
    # player : 16
    # house : 30
    firstCard = getCard("Spades", 10)
    secondCard = getCard("Spades", 10)
    thirdCard = getCard("Spades", 10)
    playerCards = [ firstCard, secondCard,thirdCard]
    house.setHand( playerCards, isKnown=True )
    firstCard = getCard("Spades", 6)
    secondCard = getCard("Spades", 10)
    houseCards = [ firstCard, secondCard]
    player.setHand( houseCards, isKnown=True )
    assert dealerHand(dealer, house, player) == 1

#all case where house win
def test_house_win():
    # Case 1: House get BlackJack hand 
    firstCard = getCard("Spades", 10)
    secondCard = getCard("Spades", 11)
    cards = [ firstCard, secondCard]
    house.setHand( cards, isKnown=True )
    dealer.dealCards(2, [player])
    assert dealerHand(dealer, house, player) == -1
    #even if player get 21 later, house still win
    firstCard = getCard("Spades", 10)
    secondCard = getCard("Spades", 9)
    thirdCard = getCard("Spades", 2)
    playerCards = [ firstCard, secondCard,thirdCard]
    player.setHand( playerCards, isKnown=True )
    assert dealerHand(dealer, house, player) == -1
    # Case 2: Player over 21 and house get 16 
    firstCard = getCard("Spades", 10)
    secondCard = getCard("Spades", 10)
    thirdCard = getCard("Spades", 10)
    playerCards = [ firstCard, secondCard,thirdCard]
    player.setHand( playerCards, isKnown=True )
    firstCard = getCard("Spades", 6)
    secondCard = getCard("Spades", 10)
    houseCards = [ firstCard, secondCard]
    house.setHand( houseCards, isKnown=True )
    assert dealerHand(dealer, house, player) == -1

def test_tie():
    # case 1: both get over 21
    firstCard = getCard("Spades", 10)
    secondCard = getCard("Spades", 10)
    thirdCard = getCard("Spades", 10)
    playerCards = [ firstCard, secondCard,thirdCard]
    house.setHand( playerCards, isKnown=True )
    firstCard = getCard("Spades", 6)
    secondCard = getCard("Spades", 10)
    thirdCard = getCard("Spades", 10)
    houseCards = [ firstCard, secondCard, thirdCard]
    player.setHand( houseCards, isKnown=True )
    assert dealerHand(dealer, house, player) == 0
    # case 2: if both get same value at 19 20 21, house stop hitting
    # 19 - 19
    firstCard = getCard("Spades", 9)
    secondCard = getCard("Spades", 10)
    playerCards = [ firstCard, secondCard]
    house.setHand( playerCards, isKnown=True )
    firstCard = getCard("Spades", 10)
    secondCard = getCard("Spades", 9)
    houseCards = [ firstCard, secondCard]
    player.setHand( houseCards, isKnown=True )
    assert dealerHand(dealer, house, player) == 0
    # 20 - 20
    firstCard = getCard("Spades", 10)
    secondCard = getCard("Spades", 10)
    cards = [ firstCard, secondCard]
    house.setHand( cards, isKnown=True )
    player.setHand( cards, isKnown=True )
    assert dealerHand(dealer, house, player) == 0
    # 21 - 21
    firstCard = getCard("Spades", 10)
    secondCard = getCard("Spades", 9)
    thirdCard = getCard("Spades", 2)
    playerCards = [ firstCard, secondCard, thirdCard]
    player.setHand( playerCards, isKnown=True )
    firstCard = getCard("Spades", 8)
    secondCard = getCard("Spades", 11)
    thirdCard = getCard("Spades", 2)
    houseCards = [ firstCard, secondCard, thirdCard]
    house.setHand( houseCards, isKnown=True )
    assert dealerHand(dealer, house, player) == 0
#check if house get more cards
def test_house_hitting():
    #case 1: house is under 16
    firstCard = getCard("Spades", 10)
    secondCard = getCard("Spades", 5)
    cards = [ firstCard, secondCard]
    house.setHand( cards, isKnown=True )
    numCard1 = len(house.hand)
    dealerHand(dealer, house, player)
    numCard2 = len(house.hand)
    assert numCard2 > numCard1

    #case 2: house is smaller than player
    firstCard = getCard("Spades", 10)
    secondCard = getCard("Spades", 6)
    cards = [ firstCard, secondCard]
    house.setHand( cards, isKnown=True )
    firstCard = getCard("Spades", 10)
    secondCard = getCard("Spades", 8)
    cards = [ firstCard, secondCard]
    player.setHand( cards, isKnown=True )
    numCard1 = len(house.hand)
    dealerHand(dealer, house, player)
    numCard2 = len(house.hand)
    assert numCard2 > numCard1

    #case 3: house is equall player and under 19
    firstCard = getCard("Spades", 10)
    secondCard = getCard("Spades", 8)
    cards = [ firstCard, secondCard]
    house.setHand( cards, isKnown=True )
    firstCard = getCard("Spades", 9)
    secondCard = getCard("Spades", 9)
    cards = [ firstCard, secondCard]
    player.setHand( cards, isKnown=True )
    numCard1 = len(house.hand)
    dealerHand(dealer, house, player)
    numCard2 = len(house.hand)
    assert numCard2 > numCard1


