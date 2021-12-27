from src.stack import Stack


class Player:
    def __init__(self, name: str):
        self.hand = Hand()
        self.name = name
        self.valid_hand = False

    @ property
    def __str__(self):
        string = self.name + " is a player with " + str(self.hand.size()) + " cards in their hand."
        return string

    def current_total(self):
        total = self.hand.total()
        return total

    def hit(self, dealer):
        dealer.deal_card(self)
        return self.current_total()

    def stick(self):
        return self.current_total()

    def hand_checker(self):
        if self.hand.total() <= 21:
            self.valid_hand = True
        else:
            self.valid_hand = False

    def get_hand_status(self):
        return self.valid_hand


class Hand(Stack):
    def __init__(self):
        super().__init__()

    def total(self):
        total = 0
        for card in self.items:
            total += card.get_value()
        return total
