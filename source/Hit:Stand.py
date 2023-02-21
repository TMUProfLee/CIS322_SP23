
def Hit_Stand(self, input, hand):
    HitStand_input = input("Hit or Stand")

    if HitStand_input == "Hit":
        hand = hand.addCard():
        return hand
    
    elif HitStand_input == "Stand":
        return hand
