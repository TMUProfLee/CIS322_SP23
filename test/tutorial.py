from testing_base import *

# Create a deck to use
deck = Deck()
# Create a dealer
dealer = Dealer(deck)

# Create players for your game

name = input("Please enter your name: ")
#runs untill else#
while True:
        #asks to confirm must use Y or N
    confirm = input("CONFIRM "+ name + "? Please enter 'Y/N':")
        #IF Y Print and end the loop
    if confirm =="Y":
        print("Awesome your username is " + name)            
        break
        #if N then ask them to re enter their name
    if confirm =="N":
        print("You have selected 'NO', please select another name....")
        name = input("Please re-enter your desired name: ")
        #if its anything else besides a Y or N make them re type their responce
    else:
        print("Looks like there was a typo in your responce, please try again and remember to use Capital letters.")

players= [Player(name)]

# Deal 5 cards to each player
dealer.dealCards(5, players)

# Show each player's hand
for player in players:
    print(f'{player.name}:')
    player.showHand(True)
    print()
player.High()