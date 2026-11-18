from uno.game import Game
from uno.player import ComputerPlayer, Player


def main():
    game = Game([Player("You"), ComputerPlayer("CPU")])


if __name__ == "__main__":
    main()
