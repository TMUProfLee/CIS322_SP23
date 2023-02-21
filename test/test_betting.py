from testing_base import *

def setup(money):
    aBox = betting_box()
    matt = Player("Matt",money)
    return aBox,matt

def test_betting_box():
    aBox,matt = setup(100)

    aBox.bet(50,matt)
    assert matt.money == 50
    assert aBox.wager == 50
    aBox.collect(0)
    assert matt.money == 100
    assert aBox.wager == 0

def test_on_a_roll():
    aBox,matt = setup(50)

    aBox.bet(50, matt)
    print(aBox.betters)
    assert matt.money == 0
    assert aBox.wager == 50
    aBox.collect(1)
    assert matt.money == 100
    assert aBox.wager == 0
    aBox.bet(100)
    assert matt.money == 0
    assert aBox.wager == 100
    aBox.collect(1)
    assert matt.money == 200
    assert aBox.wager == 0
    aBox.bet(150)
    assert matt.money == 50
    assert aBox.wager == 150
    aBox.bet(50)
    assert matt.money == 0
    assert aBox.wager == 200

def test_begger_bet():
    aBox,matt = setup(0)
    
    aBox.bet(50, matt)
    assert matt.money == 0
    assert aBox.wager == 0

def test_broke_bet():
    aBox,matt = setup(100)#matt has 100
    
    aBox.bet(50,matt)   #matt bets 50
    assert matt.money == 50
    assert aBox.wager == 50
    aBox.collect(-1)    #matt loses; the house takes the bet and thows the money away
    assert aBox.wager == 0 
    aBox.bet(50)   #matt bets 50 again
    assert matt.money == 0
    assert aBox.wager == 50
    aBox.collect(-1)    #matt loses again; the house takes the bet and thows the money away
    aBox.bet(1)    #matt tries to bet 1 on credit he is refused
    assert matt.money == 0
    assert aBox.wager == 0

def test_overdrawn():
    aBox,matt = setup(100)#matt has 100
    aBox.bet(150,matt)   #matt bets 150
    assert matt.money == 100
    assert aBox.wager == 0

