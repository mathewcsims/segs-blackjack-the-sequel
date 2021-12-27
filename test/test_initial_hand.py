import unittest
from src.deck import Deck
from blackjack import Blackjack


class InitialHandTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.game = Blackjack(deck=Deck(ace_high=False))
        self.game.add_player(name="Player 1")

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_number_of_cards(self):  # any method beginning with 'test' will be run by unittest
        number_of_cards_in_hand = self.game.player.hand.size()
        self.assertEqual(number_of_cards_in_hand, 2)


if __name__ == '__main__':
    unittest.main()
