def sumHand(self):
    handsum = 0
    for card in self.hand: 
    # loops through each card in the hand, identifies it, and then add's its value to handsum
        if card in ["J","Q","K"]:
            handsum += 10
        elif card == "A":
            handsum += 1
        else:
            handsum += int(card)
    print(handsum)

