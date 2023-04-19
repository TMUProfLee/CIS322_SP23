from CardGames import *

def test_double_down():
    betting_box = BettingBox()
    player_name = Player("player_name")
    player_name.addMoney(500)
    house = Player("house")
    bet = 250
    player_name.bet(bet)
    betting_box.collect(player_name)
    assert betting_box.total == 250
    dub_down = "y"
    betting_box.pay(player_name)
    assert betting_box.total == 0
    assert player_name.money == 1000







