from testing_base import *

"""Players"""
player = Player("player")
house = Player("house")

"""Give the players two cards each"""
five_spades = getCard("spades", 5)
six_hearts = getCard("hearts", 6)

player.addCard(five_spades)
player.addCard(six_hearts)

house.addCard(five_spades)
house.addCard(six_hearts)

"""Added functionality to showHand to allow the back of the card to be shown instead"""
def showHand(self, printShort: bool = False, showBack: bool = False):
    for idx in range(6):
        for i, card in enumerate(self.hand):
            if printShort and i < len(self.hand)-1:
                image = card.shortImage[idx] if self.knownCards[i] else card.cardBack[idx]
                print(image, end="")
            elif showBack:
                if i == 1:
                    print(card.cardBack[idx], end="")
                else:
                    image = card.image[idx]
                    print(image, end="")
    else:
        image = card.image[idx] if self.knownCards[i] else card.cardBack[idx]
        print(image, end="")
    print()


def test_showBack():
    player.showHand()
    house.showHand(printShort=True,showBack=True)
    house.showHand(showBack=True)

test_showBack()
