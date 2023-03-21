def Hit_Stand(self, Player):
  def_input = input("Would you like to Hit or Stand?  ")
    while def_input not in ["Hit", "Stand"]:
        print("Invalid input. Please enter 'Hit' or 'Stand'.")
        def_input = input("Would you like to Hit or Stand?  ")

    if def_input == 'Hit':
        Player = Player.deck.addCard()
        return Player
    elif def_input =='hit':
        Player = Player.deck.addCard()
        return Player

    elif def_input == "Stand":
        return Player
    elif def_input == "stand":
        return Player
