class Card:
    """represents a playing card"""

    COLOR_NAME = ["Clubs", "Diamonds", "Hearts", "Spades"]
    VALUE_NAME = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, value: int, color: int):
        """the card is generated"""
        self.__value = value
        self.__color = color

    # a getter function
    @property
    def value(self):
        return self.__value

    # a setter function
    @value.setter
    def value(self, value):
        self.__value = value

    # a getter function
    @property
    def color(self):
        return self.__color

    # a setter function
    @color.setter
    def color(self, color):
        self.__color = color

    def __str__(self):
        """returns a human-readable string representation"""
        return '{value} of {color}'.format(value=self.VALUE_NAME[self.value], color=self.COLOR_NAME[self.color])

    def __lt__(self, other):
        """compares this card to other, first by suit, then rank"""
        t1 = self.color, self.value
        t2 = other.color, other.value
        return t1 < t2
