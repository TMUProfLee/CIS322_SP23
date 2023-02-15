class Player:
    def __init__(self):
        self.cards = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        self.hand = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    
    def value(self, card):
        if card in self.cards[1:10]:
            return int(card)
        elif card in self.cards[10:]:
            return self.cards.index(card)+1
        else:
            return 1

########################################### 
    def sumHand(self):
        handsum = 0
        for card in self.hand: 
            handsum += self.value(card)
        return handsum
###########################################

def test_():
    hand1 = Player()
    assert hand1.sumHand() == 91
test_()