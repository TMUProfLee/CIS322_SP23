def sumHand(hand):
    handsum = 0
    for card in hand: 
    # loops through each card in the hand, identifies it, and then add's its value to handsum
        if card in ["J","Q","K"]:
            handsum += 10
        elif card == "A":
            handsum += 1
        else:
            handsum += int(card)
    return handsum

def test_answer():
    assert sumHand(["A","2","3","4","5","6","7","8","9","10","J","Q","K"]) == 85

