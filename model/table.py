import model.deck as d


class Table(d.Deck):
    """ represent the table """

    def __init__(self):
        super().__init__()
        self.__cards = []

    # a getter function
    @property
    def cards(self):
        return self.__cards

    # a setter function
    @cards.setter
    def cards(self, cards):
        self.__cards = cards
