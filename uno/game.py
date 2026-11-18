from uno.deck import Deck


class Game:
    def __init__(self, players):
        self.players = players
        self.deck = Deck()

    # Include: deal, play (main loop), next_turn, check winner
