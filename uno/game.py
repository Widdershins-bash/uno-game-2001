from uno.deck import Deck
from uno.constants import HAND_CAPACITY, MIN_PLAYERS, MAX_PLAYERS
from uno.player import Player


class Game:
    def __init__(self, players) -> None:
        self.player_count = len(players)
        if not MIN_PLAYERS <= self.player_count <= MAX_PLAYERS:
            assert ValueError(f"Expected {MIN_PLAYERS} to {MAX_PLAYERS}. Got {self.player_count}")

        self.players: list[Player] = players

        self.deck = Deck()

        self.running: bool = True
        self.active_turn: int = 0

    # Include: deal, play (main loop), next_turn, check winner

    def _deal(self) -> None:
        for player in self.players:
            while len(player.hand) < HAND_CAPACITY:

                # NOTE: I expect deck.draw() to keep track of dealt cards and remaining cards in the deck
                player.hand.append(self.deck.draw())

    def _next_turn(self) -> None:
        self.active_turn = (self.active_turn + 1) % self.player_count

    def _game_intro(self) -> str:
        intro_width: int = 45
        display: str = f"\n{intro_width * "_"}\n\n{"Welcome to Buno™":^{intro_width}}\n{intro_width * "_"}\n\n\n\n"
        return display

    def play(self) -> None:
        print(self._game_intro())

        while self.running:
            # TODO
            """
            pre: handle cases for previous played card
            1: deal cards (every round to top off)
                - first time - shuffle deck
                - if deck is empty -> move pile to deck (except for top card) -> shuffle deck
            2: display current player's cards
                - display top pile card
            3: receive current player's card choice (highlight valid selections)
                - pile should be an independent list the the last entry being the last placed card
            4: check for winner
                - if winner: display winner and end game (or create a new game cycle with a score)
            5: Go to next player
            """

            return
