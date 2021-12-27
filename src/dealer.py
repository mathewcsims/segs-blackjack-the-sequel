

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
        player.hand.push(self.deck.pop())
