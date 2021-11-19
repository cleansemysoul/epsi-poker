from Deck import Deck

"""
TODO : Add docstring
"""


class Table:
    def __init__(self, seed=None):
        deck = Deck()
        self.seed = seed if seed else deck.get_seed()
        self.deck = deck.generate_deck()
        self.bets = 0
        self.cards = []

    def get_bets(self):
        return self.bets

    def bet(self, player, amount):
        if player.remove_money(amount):
            self.bets += amount
            print(f"Bet placed {self.bets}")
        else:
            print(f"The player : {player.get_name()} can't bet {amount}, balance : {player.get_balance()}")

    def first_draw(self, players):
        for player_index, player in enumerate(players):
            for card_index, card in enumerate(self.deck):
                players[player_index].add_card(card)
                self.deck.pop(card_index)
                if card_index == 1:
                    break
        for card_index, card in enumerate(self.deck):
            self.cards.append(card)
            self.deck.pop(card_index)
            if card_index == 2:
                break

    def get_cards(self):
        return self.cards

    def __str__(self):
        return f"Table seed : {self.seed}, Cards left in the deck : {self.deck}"
