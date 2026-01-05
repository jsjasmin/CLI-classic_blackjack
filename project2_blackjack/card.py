import csv

class Card:
    '''
    Docstring for Card Class

    Represents a model for a Card in a deck.
    Handles creation of all Card objects.
    Holds a list of all instantiated cards.
    Holds a dictionary of object string pair.

    Attributes:
    rank, suit, value

    Methods:
    instantiate_from_csv() 
    ''' 
    all_cards_instantiation = [] 
    all_cards_ranksuit = []

    card_dictionary = {}

    def __init__(self, rank:str, suit:str, value=0):
        '''
        Docstring for __init__

        Attaches the following attributes to the object: rank, suit, value.
        Adds the created object to a list of all instantiated objects.
        Adds the created object to a dictionary (key: object, value: string).      

        rank -- Rank of a card
        suit -- Suit of a card (of the 4)
        value -- Value of each card according to blackjack rules
        '''
        self.rank = rank
        self.suit = suit
        self.value = value  

        Card.all_cards_instantiation.append(self)
        Card.all_cards_ranksuit.append(f"{self.rank} of {self.suit}")
        Card.card_dictionary[self] = f"{self.rank} of {self.suit}"

    @classmethod
    def instantiate_from_csv(cls):
        '''
        Docstring for instantiate_from_csv

        Instantiates all possible cards fromm a csv file.
        '''
        with open("cards.csv", "r") as card_info:
            reader = csv.DictReader(card_info)
            card_list = list(reader)
        
        for card_data in card_list:
            Card(
                rank=str(card_data.get("rank")),
                suit=str(card_data.get("suit")),
                value=int(card_data.get("value"))
            )

    def __repr__(self):
        '''
        Docstring for __repr__
        
        Changes the representation of the object.
        '''
        return f"Card('{self.rank}', {self.suit}, {self.value})"