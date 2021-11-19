"""
TODO : Add docstring
"""


class Player:
    def __init__(self, name: str, money=10):
        self.name = name
        self.cards = []
        self.money = money

    def get_name(self):
        return self.name

    def show_cards(self):
        print(self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def discard_card(self, index):
        self.cards.pop(index)

    def get_balance(self):
        return self.money

    def add_money(self, amount):
        if amount > 0:
            self.money += amount
            return True
        else:
            # Amount must be above 0
            return False
        
    def remove_money(self, amount):
        if amount > 0:
            if self.money - amount >= 0:
                self.money -= amount
                return True
            else:
                # Money can't be negative
                return False

    def __str__(self) -> str:
        return f"Name : {self.name}, Cards : {self.cards}, Money : {self.money}"