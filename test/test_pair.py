from testing_base import *

def check_hand_for_pair(aList):
    card_list=aList
    for_hand=[]
    for value in card_list:
        for_hand.append(Card("Spades", value, 'cardImages', "cardBack"))
    matt =Player('Matt')
    for card in for_hand:
        matt.addCard(card)
    return len(matt.pairCheck())

def test_for_pairs():
    assert check_hand_for_pair([1,12,3,4,5]) == 0
    assert check_hand_for_pair([1,1,3,4,5]) == 1
    assert check_hand_for_pair([1,1,1,4,5]) == 1
    assert check_hand_for_pair([1,1,1,1,1]) == 1
    assert check_hand_for_pair([1,1,3,3,3]) == 2
    assert check_hand_for_pair([1,1,]) == 1
    assert check_hand_for_pair([]) == 0