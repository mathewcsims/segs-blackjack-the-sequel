from src.stack import Stack


class Player:
    def __init__(self, name: str):
        self.hand = Hand()
        self.name = name

    @ property
    def __str__(self):
        string = self.name + " is a player with " + str(self.hand.size()) + " cards in their hand."
        return string

    def current_total(self):
        return self.hand.total()


class Hand(Stack):
    def __init__(self):
        super().__init__()

    def total(self):
        total = 0
        for card in self.items:
            total += card.get_value()
        return total
