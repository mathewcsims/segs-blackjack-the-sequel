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
        self.player.hand_checker()

    def turn(self, action):
        if action == "h":
            self.player.hit(dealer=self.dealer)
        elif action == "s":
            self.player.stick()
        else:
            pass
        self.player.current_total()
        self.player.hand_checker()


def play(ace_high=False):
    game = Blackjack(deck=Deck(ace_high=ace_high))
    game.add_player(name="Player 1")
    while game.player.get_hand_status() is True:
        action = input("Do you wish to Hit (h) or Stick (s)?")
        game.turn(action=action)


if __name__ == '__main__':
    play()
