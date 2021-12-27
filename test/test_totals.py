import unittest
from src.player import Player
from src.card import Card


# The easiest way to rig a player's score for these tests is to create some test cards and add them to the Hand
high_test_card = Card(name="Too High", suit="Test", value=22)
winning_test_card = Card(name="Twenty-One", suit="Test", value=21)
low_test_card = Card(name="Twenty-One", suit="Test", value=20)


class HighScoreTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.player = Player(name="Test Player")
        self.player.hand.push(high_test_card)

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_number_of_cards(self):  # any method beginning with 'test' will be run by unittest
        self.player.hand_checker()
        status = self.player.get_hand_status()
        self.assertEqual(status, False)


class WinningTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.player = Player(name="Test Player")
        self.player.hand.push(winning_test_card)

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_number_of_cards(self):  # any method beginning with 'test' will be run by unittest
        self.player.hand_checker()
        status = self.player.get_hand_status()
        self.assertEqual(status, True)


class LowScoreTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.player = Player(name="Test Player")
        self.player.hand.push(low_test_card)

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_number_of_cards(self):  # any method beginning with 'test' will be run by unittest
        self.player.hand_checker()
        status = self.player.get_hand_status()
        self.assertEqual(status, True)


if __name__ == '__main__':
    unittest.main()
