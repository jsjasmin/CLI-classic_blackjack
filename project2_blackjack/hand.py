from card import Card

class Hand:
    '''
    Docstring for Hand
    
    Represents the hand (cards dealt) of the player.

    Attributes:
    card_hand, card_hand_string, total_value

    Methods:
    compute_total(), is_blackjack(), is_bust()
    '''
    
    def __init__(self):
        '''
        Docstring for __init__
        
        Creates the following attributes: card_hand, card_hand_string, total_value

        card_hand -- list of Card objects
        card_hand_string -- list of the string representation of Card Objects
        total_value -- value of the whole hand
        '''
        self.card_hand = []
        self.card_hand_string = []
        self.before_hit_total_value = 0
        self.total_value = 0

    def compute_total(self):
        '''
        Docstring for compute_total
        
        Computes the total value of the hand. 
        Adjusts Ace value depending on the total value of the hand.
        '''
        total = 0
        number_of_aces = 0

        for card_in_hand in self.card_hand:
            if card_in_hand.rank == "Ace (A)":
                total = total + card_in_hand.value
                number_of_aces = number_of_aces + 1
            else:
                total = total + card_in_hand.value
                
        while total > 21 and number_of_aces > 0:
            total = total - 10
            number_of_aces = number_of_aces -1

        self.total_value = total

    def is_blackjack(self):
        '''
        Docstring for is_blackjack
        
        Checks if hand is blackjack, returns True if yes, otherwise, returns False.
        '''
        if self.total_value == 21 and len(self.card_hand) == 2:
            return True
        else:
            return False
    
    def is_bust(self):
        '''
        Docstring for is_bust
        
        Checks if hand is bust, returns True if yes, otherwise, returns False.
        '''
        if self.total_value > 21:
            return True
        else:
            return False