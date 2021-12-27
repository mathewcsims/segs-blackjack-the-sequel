from src.deck import Deck
from src.dealer import Dealer
from src.player import Player


class Blackjack:
    def __init__(self, deck):
        self.playing_deck = deck
        self.dealer = Dealer(deck=self.playing_deck)
        self.player = None

    def add_player(self, name):  # I am only supporting a single player but a list of players could be used
        self.player = Player(name=name)
        self.dealer.new_hand(player=self.player)


def play(ace_high=False):
    game = Blackjack(deck=Deck(ace_high=ace_high))
    game.add_player(name="Player 1")


if __name__ == '__main__':
    play()
