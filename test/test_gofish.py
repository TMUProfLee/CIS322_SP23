from testing_base import *
import random

def test_gofish():
    camila = Player('Camila')
    kaylie = Player('Kaylie')
    john = Player('John')
    players = [camila, kaylie, john]

    s_5 = Card("Spades", 5, "None", "None")
    h_5 = Card("Hearts", 5, "None", "None")
    h_8 = Card("Hearts", 8, "None", "None")
    c_8 = Card("Clubs", 8, "None", "None")
    c_2 = Card("Clubs", 2, "None", "None")
    deck = []

    camila.hand = [s_5, s_5, s_5, s_5, s_5]
    kaylie.hand = [h_5, h_5, h_8, c_2, s_5]
    john.hand = [s_5, h_5, c_8, c_2, s_5]

    info = [[camila, [s_5, s_5, s_5, s_5, s_5]], [kaylie, [h_5, h_5, h_8, c_2, s_5]], [john, [s_5, h_5, c_8, c_2, s_5]]]

    #Surrender Card: If player asked has the card, it will return True
    #Go Fish: if player asked does not have the card, it will return None 
    assert GoFish.ask_Card(8, "Hearts", info, camila, kaylie) == True
    assert GoFish.ask_Card(7, "Hearts", info, camila, kaylie) == None
    assert GoFish.ask_Card(2, "Clubs", info, camila, john) == True

    #John has an 8 clubs but not an 8 hearts, so it returns none
    assert GoFish.ask_Card(8, "Hearts", info, camila, john) == None
    assert GoFish.ask_Card(8, "Clubs", info, camila, john) == True
    assert GoFish.ask_Card(5, "Spades", info, john, camila) == True 
    
    

test_gofish()
