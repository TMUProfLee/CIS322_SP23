def sumHand(self):
    handsum = 0
    for card in self.hand: 
        handsum += card.value
    return handsum

