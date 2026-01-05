from card import Card
import random

class Deck:
    '''
    Docstring for Deck

    Represents a model of a deck of cards.

    Attributes:
    card_deck, removed_card_for_the_round

    Methods: 
    shuffle(), deal()
    '''
    main_deck = ""

    def __init__(self):
        '''
        Docstring for __init__
        
        Creates the following attributes: card_deck, removed_card_for_the_round.

        card_deck -- a list of all the card object (52-card deck)
        removed_card_for_the_round -- list of all dealt/ removed from the deck cards
        '''
        self.card_deck = Card.all_cards_instantiation
        self.removed_card_for_the_round = []

        Deck.main_deck = self

    def shuffle(self):
        '''
        Docstring for shuffle
        
        Adds the removed/ dealt cards back to the card_deck.
        Shuffles the arrangement of the cards in the list.
        '''
        self.card_deck.extend(self.removed_card_for_the_round)
        self.removed_card_for_the_round.clear()
        random.shuffle(self.card_deck)

    def deal(self):
        '''
        Docstring for deal
        
        Gets the topmost card (first card) and removes it from the deck.
        Returns the topmost card to be added to a hand.
        '''
        dealt_card = self.card_deck[0]
        self.removed_card_for_the_round.append(dealt_card)
        self.card_deck.remove(dealt_card)
        return dealt_card
