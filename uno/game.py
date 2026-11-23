from uno.deck import Deck
from uno.constants import HAND_CAPACITY


class Game:
    def __init__(self, players) -> None:
        self.players = players
        self.deck = Deck()

        self.running: bool = True

    # Include: deal, play (main loop), next_turn, check winner

    def deal(self) -> None:
        for player in self.players:
            while len(player.hand) < HAND_CAPACITY:
                player.hand.append(self.deck.draw())

    def play(self) -> None:
        # draw new cards at the start of every round
        while self.running:
            ...
