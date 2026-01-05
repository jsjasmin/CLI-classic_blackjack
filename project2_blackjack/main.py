from card import Card
from deck import Deck
from game import BlackjackGame

if __name__ == "__main__":
    Card.instantiate_from_csv()
    Deck()
    BlackjackGame.start()
