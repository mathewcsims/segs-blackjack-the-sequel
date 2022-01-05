from src.deck import Deck
from src.dealer import Dealer
from src.player import Player
import src.interactions as interactions


class Blackjack:
    def __init__(self, deck):
        self.playing_deck = deck
        self.dealer = Dealer(deck=self.playing_deck)
        self.player = None

    def add_player(self, name, test=False):  # I am only supporting a single player but a list could be used
        self.player = Player(name=name)
        self.dealer.new_hand(player=self.player, test=test)
        self.player.hand_checker()

    def turn(self, action) -> None:
        if action == "h":
            self.player.hit(dealer=self.dealer)
        elif action == "s":
            self.player.stick()
        else:
            pass
        self.player.current_total()
        self.player.hand_checker()


def play() -> None:

    interactions.instructions()
    game = Blackjack(deck=Deck(ace_high=interactions.set_ace_default()))

    # This is a single player only version of the game. If multiple players were implemented,
    # then this and the rest of the play() function from here on need redoing to accommodate that.
    game.add_player(name=interactions.choose_player_name())

    interactions.initial_hand()

    keep_playing = game.player.get_hand_status()

    while keep_playing is True and game.player.current_total() < 21:
        game.player.print_hand()
        action = interactions.hit_or_stick()
        game.turn(action=action)
        keep_playing = game.player.get_hand_status()
        if action == "s":
            keep_playing = False
        if not keep_playing:
            break

    interactions.end_game(player=game.player)


if __name__ == '__main__':
    play()
