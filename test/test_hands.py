import unittest
from src.player import Player
from src.card import Card


# The easiest way to rig a player's hand for these tests is to create some test cards and add them to the Hand
king = Card(name="King", suit="Test", value=10)
high_ace = Card(name="Ace", suit="Test", value=11)
low_ace = Card(name="Ace", suit="Test", value=1)
queen = Card(name="Queen", suit="Test", value=10)
nine = Card(name="Nine", suit="Test", value=9)


class HandsTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.player = Player(name="Test Player")

    def tearDown(self):  # this method will be run after each tests
        del self.player

    def test_hand1(self):  # any method beginning with 'test' will be run by unittest
        self.player.hand.push(king)
        self.player.hand.push(high_ace)
        self.assertEqual(self.player.current_total(), 21)

    def test_hand2(self):  # any method beginning with 'test' will be run by unittest
        self.player.hand.push(king)
        self.player.hand.push(queen)
        self.player.hand.push(low_ace)
        self.assertEqual(self.player.current_total(), 21)

    def test_hand3(self):  # any method beginning with 'test' will be run by unittest
        self.player.hand.push(nine)
        self.player.hand.push(high_ace)
        self.player.hand.push(low_ace)
        self.assertEqual(self.player.current_total(), 21)


if __name__ == '__main__':
    unittest.main()
