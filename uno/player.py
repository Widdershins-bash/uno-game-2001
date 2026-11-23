from uno.card import Card


class Player:
    def __init__(self, name) -> None:
        self.name: str = name
        self.hand: list[Card] = []

    # Include: choose_card (human picks via input())


class ComputerPlayer(Player):
    pass

    # Include: choose_card (picks automatically)
