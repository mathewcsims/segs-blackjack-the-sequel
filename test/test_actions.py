import unittest
from src.deck import Deck
from blackjack import Blackjack


class ActionsTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.game = Blackjack(deck=Deck(ace_high=False))
        self.game.add_player(name="Player 1", test=True)

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_hit(self):  # any method beginning with 'test' will be run by unittest
        initial_total = self.game.player.current_total()
        self.game.turn(action="h", test=True)
        after_total = self.game.player.current_total()
        self.assertFalse(initial_total == after_total)

    def test_stick(self):  # any method beginning with 'test' will be run by unittest
        initial_total = self.game.player.current_total()
        self.game.turn(action="s")
        after_total = self.game.player.current_total()
        self.assertEqual(initial_total, after_total)


if __name__ == '__main__':
    unittest.main()
