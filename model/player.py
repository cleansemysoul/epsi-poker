import abc


class Player:
    """ represent a player, parent class """

    def __init__(self, name: str, chips: int):
        self.__name = name
        self.__chips = chips
        self.__hand = []

    # a getter function
    @property
    def name(self):
        return self.__name

    # a setter function
    @name.setter
    def name(self, name):
        self.__name = name

    # a getter function
    @property
    def chips(self):
        return self.__chips

    # a setter function
    @chips.setter
    def chips(self, chips):
        self.__chips = chips

    # a getter function
    @property
    def hand(self):
        return self.__hand

    # a setter function
    @hand.setter
    def hand(self, hand):
        self.__hand = hand
