class Player:
    def __init__(self, name: str, money=10):
        self.name = name
        self.cards = []
        self.money = money

    def who_am_i(self):
        print(self.name)

    def show_cards(self):
        print(self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def discard_card(self, index):
        self.cards.pop(index)

    def get_balance(self):
        print(self.money)

    def add_money(self, amount):
        if amount > 0:
            self.money += amount
        else:
            print("Amount must be above 0")
        
    def remove_money(self, amount):
        if amount > 0:
            if self.money - amount >= 0:
                self.money -= amount
            else:
                print("Money can't be negative")

    def __str__(self) -> str:
        return f"Name : {self.name}, Cards : {self.cards}, Money : {self.money}"