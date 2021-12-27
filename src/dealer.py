

class Dealer:
    def __init__(self, deck):
        self.deck = deck
        self.shuffle_deck()

    def shuffle_deck(self):
        self.deck.shuffle()

    def new_hand(self, player):
        for i in range(2):
            player.hand.push(self.deck.pop())
        player.valid_hand = True

    def deal_card(self, player):
        dealt_card = self.deck.pop()
        if dealt_card.get_name() == "Ace":
            answer = input("You got an Ace. Enter what you want it to be worth (1 or 11)")
            if answer == 1:
                dealt_card.set_value(1)
            elif answer == 11:
                dealt_card.set_value(11)
            else:
                print("You didn't enter a valid answer, so I'll leave the value as the default",
                      str(dealt_card.get_value()))
        player.hand.push(dealt_card)
