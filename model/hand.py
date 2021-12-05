import model.deck as d


class Hand(d.Deck):
    """represents a hand of playing cards."""

    def __init__(self, label=''):
        super().__init__()
        self.__label = label
        self.__cards = []

    # a getter function
    @property
    def label(self):
        return self.__label

    # a setter function
    @label.setter
    def label(self, label):
        self.__label = label

    # a getter function
    @property
    def cards(self):
        return self.__cards

    # a setter function
    @cards.setter
    def cards(self, cards):
        self.__cards = cards
