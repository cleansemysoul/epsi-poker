import random

"""
TODO : Add docstring
"""


class Deck:
    def __init__(self):
        self.suits = ["Heart", "Diamonds", "Spades", "Clubs"]
        self.values = {
                        "2": "2",
                        "3": "3",
                        "4": "4",
                        "5": "5",
                        "6": "6",
                        "7": "7",
                        "8": "8",
                        "9": "9",
                        "10": "10",
                        "Jack": "11",
                        "Queen": "12",
                        "King": "13",
                        "Ace": "14"
                       }
        self.seed = random.randint(0, 20000)

    def __build(self):
        cards = []
        for suit in self.suits:
            for key in self.values:
                card = [suit, key, self.values[key]]
                cards.append(card)
        return cards

    def generate_deck(self):
        random.seed(self.seed)
        new_deck = self.__build()
        random.shuffle(new_deck)
        return new_deck

    def get_seed(self):
        return self.seed
