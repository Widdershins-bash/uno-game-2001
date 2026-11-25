import unittest

from uno.game import Game
from uno.player import ComputerPlayer, Player


class TestGame(unittest.TestCase):

    def test_init(self):
        players = [Player("You"), ComputerPlayer("CPU")]
        self.assertEqual(Game(players).players, players)

    def test_display(self) -> None:
        players = [Player("You"), ComputerPlayer("CPU")]
        for player in players:
            ...


if __name__ == "__main__":
    unittest.main()
