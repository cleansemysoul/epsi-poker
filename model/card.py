class Card:
    """represents a playing card"""
    COLOR_NAME = ["Clubs", "Diamonds", "Hearts", "Spades"]
    VALUE_NAME = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.showing = True

    def __repr__(self):
        return (f"{self.value} {self.suit}")
        
    @property
    def color(self):
        return self.__color

    # a setter function
    @color.setter
    def color(self, color):
        self.__color = color

    def __str__(self):
        """returns a human-readable string representation"""
        return f'{self.value} of {self.suit}'

    def __lt__(self, other):
        """compares this card to other, first by suit, then rank"""
        t1 = self.suit, self.value
        t2 = other.suit, other.value
        return t1 < t2