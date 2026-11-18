import unittest

from uno.deck import Deck


class TestDeck(unittest.TestCase):
    def test_init(self):
        self.assertIsInstance(Deck().cards, list)


if __name__ == "__main__":
    unittest.main()
