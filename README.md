# Classic BlackJack: CLI Edition
A command-line interface (CLI) blackjack game built using python, with classic rules and computer players. 

# Features
* Play Classic Blackjack in CLI against a computer Dealer
* Stylized user interface with textual representation of cards.
* A Blackjack variation, implementing standard Hit and Stand actions.
* Multiple Players, you and other computer players (up to 9 bots).

# Prerequisites
* Python 3.8 or higher installed on your machine
* No external dependencies required

# Usage
To run the game locally, clone the repository and run `python main.py` in the terminal.
```bash
# From git bash, clone repository and run main.py
git clone https://github.com/jsjasmin/CLI-classic_blackjack.git
cd CLI-classic_blackjack/project2_blackjack
python main.py
```
It is recommended to full screen the bash with font style Consolas 9pt.
### Screen Capture of the Title Screen
<img width="1095" height="506" alt="image" src="https://github.com/user-attachments/assets/2b26b3f0-8ab8-44c2-9e96-a9763a15fb61" />

# Gameplay

**Initial Setup**
* Players place bets before any cards are dealt.
* Dealer gives two cards to each player and themselves.
* Dealer’s second card remains hidden from players.

**Card Hand**
  * _Card Values_
      * Number cards (2–10): Face value.
      * Face cards (Jack, Queen, King): Value of 10.
      * Aces: Can be 1 or 11, whichever is more beneficial.
  
  * _BlackJack Hand (Instant Win)_
      * A two-card total of 21 is a BlackJack.
      * Payout: 1.5 × bet plus original bet returned (3:2 odds).
      * Example: Bet $50 -> win $125 total.
  
  * _Non-BlackJack Hand (Player Choices)_
      * Hit: Take another card.
      * Stand: End turn.

  * _Bust_
      * Hand value over 21 -> lose immediately.

**Dealer’s Turn**
* Reveals hidden card after all players finish.
* Must hit if hand value is less than 16.
* Must stand at 17 or higher.

**Winning Conditions**
* Dealer busts: All remaining players win 2× bet (1:1).
* No dealer bust: Players with higher hand value than dealer win 2× bet (1:1).

**Round End**
* Winnings distributed.
* Players choose to continue or end game.


# Project Structure
```
CLI-classic_blackjack/
├── project2_blackjack/
│   ├── main.py                # Entry point, initializes and starts the game
│   ├── game.py                # Main game engine and game loop, Blackjackgame class
│   ├── player.py              # Player class with hit, stand, and betting logic
│   ├── dealer.py              # Dealer class AI
│   ├── card.py                # Card Class, instantiates Card objects
│   ├── card.csv               # Card data for instantiation in card.py
│   ├── deck.py                # Deck Class, holds card objects with shuffling and dealing 
│   ├── hand.py                # Hand class for holding dealt cards and computing values
│   └── helper_functions.txt   # Utility functions
└── README.md                  # This file
```
# Class Description and Responsibilities

`Blackjackgame` manages game loop/ flow and outputs. `Player` handles inputs for decisions of betting and hit/ stand. `Computer_player` manages decisions for betting and actions for bot players. `Dealer` follows a ruleset for hitting/ standing. `Card` creates card objects and handles rank, suit, and value. `Deck` holds a list of all card objects and handles shuffling and dealing. `Hand` manages dealt cards from Deck to Player and computes total hand value (for win conditions and blackjack/bust)

|      Class      |    File   |                                 Summary                                |
|:---------------:|:---------:|:----------------------------------------------------------------------:|
| Blackjackgame   | game.py   | Main game engine, manages game loop and flow                           |
| Player          | player.py | Human player with hit, stand, and betting logic                        |
| Computer_player | player.py | Child class of Player, bot players capable of decision logic from a ruleset |
| Dealer          | dealer.py | Specialized AI which follows a set of rules                            |
| Card            | card.py   | Model of a card, handles creation of all Card objects                  |
| Deck            | deck.py   | Represents a deck of cards, with shuffling and dealing                 |
| Hand            | hand.py   | Hand of Player objects, holds dealt cards and computes values          |

# Game Flow

```python
# From main.py
if __name__ == "__main__":
    Card.instantiate_from_csv()
    Deck()
    BlackjackGame.start()

# From game.py Blackjackgame class, the start() method runs the game loop
  @classmethod
  def start(cls):
      cls.opening_display()
      Deck.main_deck.shuffle()
      cls.setup_players()
      while True:
          cls.place_bets()
          cls.initial_deal()
          cls.run_player_turns()
          cls.run_dealer_turn()
          cls.resolve_round()
          cls.eliminate_bankrupt_players()
          if not cls.ask_continue():
              cls.ending_display()
              break

          cls.round_number += 1
          cls.reset_for_next_round()    
```
* `Card.instantiate_from_csv()` - instantiates all Card objects
* `Deck()` - istantiates a Deck object
* `cls.opening_display()` - outputs title screen and How-Tos
* `Deck.main_deck.shuffle()` - shuffles main_deck object
* `cls.setup_players()` - instantiates Player and Computer_player from player input of name and # of bots
* `cls.place_bets()` - asks player and Computer_player objects for round bet
* `cls.initial_deal()` - deals 2 cards to each player and dealer, and outputs initial deal summary
* `run_player_turns()` - asks each player for round action
* `run_dealer_turns()` - after reveal, acts accordingly according to ruleset
* `resolve_round()` - computes wins and loss, and balance and bet values
* `eliminate_bankrupt_players()` - removes bankrupt players from the game
* `cls.ask_continue()` - asks player if continuing to next round (back to  `cls.place_bets()`)
* `cls.ending_display()` - if not continuing, shows credits
* `cls.reset_for_next_round()` - shuffles deck, and resets and clears attributes

## Contributing

Contributions are highly welcome and is greatly appreciated. If you find any bugs and suggestions for code optimization, feel free to submit a pull request. Thank you!

## Author and Credits

#### Created by
I am Jose Mari Jasmin Jr., an undergraduate students tudying BS Computer Engineering,
from University of the Philippines Diliman.

- Personal Email: jasmin.josemarijr@gmail.com
- School Email: jsjasmin2@upd.edu.ph

#### Special Thanks 
- ASCII art from [Text to ASCII Art Generator (patorjk.com)](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type+&x=none&v=4&h=4&w=80&we=false)

- Random Names from [250 Best Funny Usernames—Cool, Clever Usernames (parade.com)](https://parade.com/1032891/marynliles/funny-usernames/)
