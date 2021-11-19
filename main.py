from Deck import Deck
from Player import Player

players = [Player("Player 1"), Player("Player 2"), Player("Player 3"), Player("Player 4")]

deck = Deck()
deck = deck.generate_deck()


def generate_hands(players : []):
    for player_index, player in enumerate(players):
        count = 0
        for card_index, card in enumerate(deck):
            players[player_index].add_card(card)
            deck.pop(card_index)
            count += 1
            if count == 2:
                break


generate_hands(players)


for player in players:
    player.who_am_i()
    player.show_cards()