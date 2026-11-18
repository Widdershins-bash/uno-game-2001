# UNO (terminal)

UNO with a terminal interface and computer opponent(s). Standard library only — no installs needed.

## Developers
- Kaden
- Nimco

## Project layout
```
main.py            entry point
uno/
  card.py          Card class
  deck.py          Deck (draw pile)
  player.py        Player, ComputerPlayer
  game.py          Game state + main loop
tests/             unittest tests (test_<module>.py)
```

## Run
```
python main.py
```

## Test
Run from the project root:
```
python -m unittest -v
```
