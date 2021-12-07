import random
import model.card as c


class Deck:
    """represents a card game"""

    def __init__(self):
        """initializes the pack with 52 cards"""
        self.__cards = []
        for color in range(4):
            for value in range(1, 14):
                card = c.Card(value, color)
                self.__cards.append(card)

    # a getter function
    @property
    def cards(self):
        return self.__cards

    # a setter function
    @cards.setter
    def cards(self, cards):
        self.__cards = cards

    def __str__(self):
        """returns a string representation of the game"""
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def shuffle_cards(self, seed: int):
        """shuffles the cards in this game"""
        random.seed(seed)
        random.shuffle(self.cards)

    def sort_cards(self):
        """sorts the cards in ascending order."""
        self.cards.sort()

    def pop_card(self, i=-1):
        """removes and returns a card from the game
        i: index of the card to pop; by default, pops the last card.
        """
        return self.cards.pop(i)

    def add_card(self, card):
        """adds a card to the game"""
        self.cards.append(card)

    def remove_card(self, card):
        """Removes a card from the deck or raises exception if it is not there"""
        self.cards.remove(card)

    def move_cards(self, hand, num: int):
        """moves the given number of cards from the game into the hand.

        hand: destination Hand object
        num: integer number of cards to move
        """
        for i in range(num):
            hand.add_card(self.pop_card())
