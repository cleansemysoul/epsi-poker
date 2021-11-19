import random


class Deck:
    def __init__(self):
        self.suits = ["Coeur", "Carreaux", "Pique", "Trèfle"]
        self.values = {
                        "As": "A",
                        "2": "2",
                        "3": "3",
                        "4": "4",
                        "5": "5",
                        "6": "6",
                        "7": "7",
                        "8": "8",
                        "9": "9",
                        "10": "10",
                        "Valet": "J",
                        "Dame": "Q",
                        "Roi": "K"
                       }

    def __build(self):
        cards = []
        for suit in self.suits:
            for key in self.values:
                card = [suit, key, self.values[key]]
                cards.append(card)
        return cards

    def get_deck(self) -> []:
        new_deck = self.__build()
        random.shuffle(new_deck)
        return new_deck