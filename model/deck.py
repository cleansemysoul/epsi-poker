import random
import model.card as card

class Deck:
    def __init__(self):
        self.suits = ["Heart", "Diamonds", "Spades", "Clubs"]
        self.values = ["2","3","4","5","6","7","8","9","10","11","12","13","14"]
        self.seed = random.randint(0, 20000)

    def __build(self):
        cards = []
        for suit in self.suits:
            for value in self.values:
                new_card = card.Card(suit, value)
                cards.append(new_card)
        return cards

    def generate_deck(self):
        random.seed(self.seed)
        new_deck = self.__build()
        random.shuffle(new_deck)
        return new_deck

    def get_seed(self):
        return self.seed