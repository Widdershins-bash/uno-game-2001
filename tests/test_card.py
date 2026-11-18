import unittest

from uno.card import Card


class TestCard(unittest.TestCase):
    def test_init(self):
        card = Card("red", "5")
        self.assertEqual(card.color, "red")
        self.assertEqual(card.value, "5")


if __name__ == "__main__":
    unittest.main()
