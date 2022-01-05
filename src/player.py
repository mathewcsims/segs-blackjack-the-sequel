from src.stack import Stack
from src.interactions import end_game


class Player:
    def __init__(self, name: str):
        self.hand = Hand()
        self.name = name
        self.valid_hand = False

    def __str__(self) -> str:
        string = self.name + " is a player with " + str(self.hand.size()) + " cards in their hand."
        return string

    def current_total(self) -> int:
        total = self.hand.total()
        return total

    def hit(self, dealer, test=False) -> int:
        dealer.deal_card(self, test=test)
        return self.current_total()

    def stick(self) -> None:  # This doesn't really need to be here, but might be useful for other variations
        pass

    # checks if a hand is <=21, if so sets valid_hand to true, false if not
    def hand_checker(self) -> None:
        if self.hand.total() <= 21:
            self.valid_hand = True
        else:
            self.valid_hand = False

    # returns true if the player has a valid hand, false if not
    def get_hand_status(self) -> bool:
        return self.valid_hand

    def print_hand(self, end=False):
        if end:
            print(self.name + ",", "your final hand consisted of", str(self.hand.size()), "cards. They were:")
        else:
            print(self.name + ",", "your hand consists of", str(self.hand.size()), "cards. They are:")
        print(self.hand)


class Hand(Stack):
    def __init__(self):
        super().__init__()

    def total(self) -> int:
        total = 0
        for card in self.items:
            total += card.get_value()
        return total

    def __str__(self) -> str:
        string: str = "Total: " + str(self.total())
        for card in self.items:
            print("* " + str(card))
        return string
