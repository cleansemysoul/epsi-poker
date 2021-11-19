from Deck import Deck
import Player

deck = Deck()
deck = deck.get_deck()
print(len(deck))

players = ["Player 1", "Player 2", "Player 3", "Player 4"]
player_hand = []
for player_index, player in enumerate(players):
    hand = []
    for card_index, card in enumerate(deck):
        hand.append(card)
        deck.pop(card_index)
        if len(hand) == 5:
            break
    print(len(hand))
    print(hand)

print(player_hand)

