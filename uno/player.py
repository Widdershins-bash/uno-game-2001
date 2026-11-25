from uno.card import Card


class Player:
    def __init__(self, name) -> None:
        self.name: str = name
        self.hand: list[Card] = []

    def display_hand(self) -> str:
        outline_partial: str = ""
        card_partial: str = ""

        for i, card in enumerate(self.hand):
            card_len: int = len(str(card))

            outline_partial += f"{'':6}{card_len * "_"} "
            card_partial += f" {i:>2}: | {card} |"

        return f"{outline_partial}\n{card_partial}\n{outline_partial}"

    # Include: choose_card (human picks via input())
    def choose_card(self) -> Card: ...


class ComputerPlayer(Player):
    pass

    # Include: choose_card (picks automatically)
