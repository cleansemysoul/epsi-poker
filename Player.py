class Player:
    def __init__(self, name: str):
        self.name = name
        self.cards = []

    def who_am_i(self):
        print(self.name)

    def add_card(self, card):
        self.cards.append(card)

    def show_cards(self):
        print(self.cards)