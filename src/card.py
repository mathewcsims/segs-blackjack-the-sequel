class Card:
    def __init__(self, name: str, value: int, suit: str):
        self.name = name
        self.value = value
        self.suit = suit

    def get_value(self) -> int:
        return self.value

    def set_value(self, value: int):
        self.value = value

    def get_name(self):
        return self.name

    @property
    def __str__(self):
        string = self.name + " of " + self.suit
        return string
