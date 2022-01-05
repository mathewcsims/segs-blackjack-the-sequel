class Dealer:
    def __init__(self, deck):
        self.deck = deck
        self.shuffle_deck()

    def shuffle_deck(self) -> None:
        self.deck.shuffle()

    def new_hand(self, player, test=False) -> None:
        for i in range(2):
            self.deal_card(player=player, test=test)
        player.valid_hand = True

    def deal_card(self, player, test=False) -> None:
        dealt_card = self.deck.pop()
        if dealt_card.get_name() == "Ace" and not test:
            answer = int(input("You got an Ace. Enter what you want it to be worth (1 or 11)"))
            if answer == 1:
                dealt_card.set_value(1)
            elif answer == 11:
                dealt_card.set_value(11)
            else:
                print("You didn't enter a valid answer, so I'll leave the value as the default",
                      str(dealt_card.get_value()))
        player.hand.push(dealt_card)
