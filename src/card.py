class Card:
    def __init__(self, name: str, value: int, suit: str):
        self.name = name
        self.value = value
        self.suit = suit

    def get_value(self) -> int:
        return self.value

    def set_value(self, value: int) -> None:
        self.value = value

    def get_name(self) -> str:
        return self.name

    def __str__(self) -> str:
        string = self.name + " of " + self.suit
        return string
