
def Hit_Stand(self, Player):
    def_input = input("Would you like to Hit or Stand?  ")

    if def_input == 'Hit':
        Player = Player.deck.addCard()

        return Player

    if def_input == "Stand":

        return Player
    