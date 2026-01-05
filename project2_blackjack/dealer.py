from player import Player
from helper_functions import ask_player_input
from deck import Deck
from hand import Hand
from card import Card
from hand import Hand

class Dealer:
    '''
    Docstring for Dealer

    Represents a model for a Dealer and its behaviour.

    Attributes:
    name, hand

    Methods:
    play_turn(),  hit(deck), hit_stand_after_reveal() 
    '''
    main_dealer = ""

    def __init__(self, name):
        '''
        Docstring for __init__
        
        Attaches the following attributes to the object: name, hand.
        Sets the instantiated Dealer to be the main_dealer for the game.

        name -- name of the dealer
        hand -- list of cards in the hand
        '''
        self.name = name
        self.hand = Hand()

        Dealer.main_dealer = self

    def play_turn(self):
        '''
        Docstring for play_turn
        
        Hits twice during initial_deal.
        '''
        self.hit(Deck.main_deck)
        self.hit(Deck.main_deck)

    def hit(self, deck):
        '''
        Docstring for hit
        
        Obtains a card from the deck and adds it to the hand of the object.
        
        deck -- deck object to get the card
        '''
        dealt_card = deck.deal()

        self.hand.card_hand.append(dealt_card)
        self.hand.card_hand_string.append(Card.card_dictionary[dealt_card])
        return True

    def hit_stand_after_reveal(self):
        '''
        Docstring for hit_stand_after_reveal
        
        Hits if hand value is >= 17, otherwise, Stands.
        '''

        if self.hand.total_value < 17:
            self.hit(Deck.main_deck)
            return 1
        else:
            return 2