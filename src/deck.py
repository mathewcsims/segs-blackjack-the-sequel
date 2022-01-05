from src.stack import Stack
from src.card import Card
import random

# Define the suits and values of cards in a standard pack
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
values = [
    ("Ace", 1),
    ("Two", 2),
    ("Three", 3),
    ("Four", 4),
    ("Five", 5),
    ("Six", 6),
    ("Seven", 7),
    ("Eight", 8),
    ("Nine", 9),
    ("Ten", 10),
    ("Jack", 10),
    ("King", 10),
    ("Queen", 10)
]
# And values for if the player chooses aces should be 11 by default
values_high = [
    ("Two", 2),
    ("Three", 3),
    ("Four", 4),
    ("Five", 5),
    ("Six", 6),
    ("Seven", 7),
    ("Eight", 8),
    ("Nine", 9),
    ("Ten", 10),
    ("Jack", 10),
    ("King", 10),
    ("Queen", 10),
    ("Ace", 11),
]


class Deck(Stack):
    def __init__(self, ace_high=False):  # `ace_high' flag to control whether ace defaults to 1 (False) or 11 (True)
        super().__init__()
        if ace_high is True:
            values_active = values_high
        else:
            values_active = values
        for suit in suits:
            for value in values_active:
                card = Card(name=value[0],
                            value=value[1],
                            suit=suit)
                self.push(card)

    def shuffle(self) -> None:
        shuffled_deck = []
        original_deck = self.items
        number_of_cards = self.size()
        n = 1
        while n <= number_of_cards:
            random_card = random.randrange(len(original_deck))
            card = original_deck[random_card]
            shuffled_deck.append(card)
            del original_deck[random_card]
            n += 1
        del original_deck
        self.items = shuffled_deck
        del shuffled_deck

    def __str__(self) -> str:
        string = "This is a deck of " + str(self.size()) + " cards."
        for card in self.items:
            print(card)
        return string
