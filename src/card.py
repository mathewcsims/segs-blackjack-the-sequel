class Card:
    def __init__(self, name: str, value: int, suit: str):
        self.name = name
        self.value = value
        self.suit = suit

    def get_value(self) -> int:
        return self.value

    @property
    def __str__(self):
        string = self.name + " of " + self.suit
        return string
