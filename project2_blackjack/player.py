from helper_functions import ask_player_input
from helper_functions import give_random_number_bet
from deck import Deck
from card import Card
from hand import Hand


class Player: 
    '''
    Docstring for Player
    
    Represents a model for a player in the game.
    Holds a list of all instantiated players.
    Holds a dictionary of object string pair.

    Attributes:
    name, balance, bet, hand

    Methods::
    place_bet(), hit(deck), stand(), ask_turn_decision(), check_hands_player_dealer(dealer)
    '''
    all_players = []
    all_players_immutable = []

    def __init__(self, name:str, balance:float, bet=0):
        '''
        Docstring for __init__
        
        Attaches the following attributes to the object: name, balance, bet, hand.
        Adds the created object to a list of all instantiated objects.
        Adds the created object to a dictionary (key: object, value: string).      

        name -- name of the player object
        balance -- remaining money of the player
        bet -- bet of the player for the round
        hand -- list of cards in the hand
        round_status -- hit or stand depending on decision during turn
        '''
        self.name = name
        self.balance = balance
        self.previous_round_balance = balance
        self.bet = bet
        self.hand = Hand()
        self.round_status = "To play."

        Player.all_players.append(self)
        Player.all_players_immutable.append(self)


    def place_bet(self):
        '''
        Docstring for place_bet
        
        Changes the bet attribute of the player, and subtracts it to the balance.
        '''
        self.bet = int(ask_player_input("Please enter your Round Bet ($): ","integer", "player_bet", self.balance))
        self.balance = self.balance - self.bet

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

    def stand(self):
        '''
        Docstring for stand
        
        Does nothing for the player turn.
        '''
        return 
    
    def ask_turn_decision(self):
        '''
        Docstring for ask_turn_decision
        
        Asks for the decision of the Player during player turn.
        If 1, hits, if 2, stands.
        '''
        turn_decision = int(ask_player_input("Your Turn Decision: (1: Hit | 2: Stand)", "integer", "decision"))
        if turn_decision == 1:
            self.hit(Deck.main_deck)
            return 1
        elif turn_decision == 2:
            self.stand()
            return 2

    def check_hands_player_dealer(self, dealer):
        '''
        Docstring for check_hands_player_dealer
        
        Checks who won, player or dealer, during the round.

        dealer -- the compared to hand value to determine if won or lost
        '''
        self.hand.compute_total()
        dealer.hand.compute_total()
        player_hand_value = self.hand.total_value
        dealer_hand_value = dealer.hand.total_value


        if dealer.hand.is_blackjack() and self.hand.is_blackjack():
            self.balance = self.balance + self.bet
        elif dealer.hand.is_blackjack() and not self.hand.is_blackjack():
            self.balance = self.balance
        elif self.hand.is_blackjack() and not dealer.hand.is_blackjack():
            self.balance = self.balance + self.bet + (self.bet * 1.5)

        elif self.hand.is_bust():
            self.balance = self.balance
        elif dealer.hand.is_bust() and not self.hand.is_bust():
            self.balance = self.balance + self.bet + self.bet
        
        elif player_hand_value > dealer_hand_value:
            self.balance = self.balance + self.bet + self.bet
        elif dealer_hand_value > player_hand_value:
            self.balance = self.balance

        elif dealer_hand_value == player_hand_value:
            self.balance = self.balance + self.bet
    
    def __repr__(self):
        return f"Player('{self.name}', '{self.balance}', '{self.hand}', '{self.bet}')"

class Computer_Player(Player): 
    '''
    Docstring for Computer_Player
        
    A child class of Player.
    Represents a model for a Computer player in the game.

    Attributes:
    name, balance, bet, hand

    Methods::
    place_bet(), hit(deck), stand(), ask_turn_decision(), check_hands_player_dealer(dealer)

    '''
    def place_bet(self):
        '''
        Docstring for place_bet
        
        Changes the bet attribute of the player, and subtracts it to the balance.
        Uses the give_random_number_bet to obtain a bet.
        '''
        self.bet = int(give_random_number_bet(self.balance)) 
        self.balance = self.balance - self.bet

    def ask_turn_decision(self):
        '''
        Docstring for ask_turn_decision
        
        Asks for the decision of the Player during player turn.
        If 1, hits, if 2, stands.
        Uses give_random_number_bet but restricts to either 1 or 2.
        '''
        
        if self.hand.total_value < 17:
            self.hit(Deck.main_deck)
            return 1
        else:
            self.stand()
            return 2





