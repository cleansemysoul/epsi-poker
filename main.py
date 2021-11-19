from Player import Player
from Table import Table

player = Player("Human")
bot_first = Player("IA 1")
bot_second = Player("IA 2")
bot_third = Player("IA 3")

players = [player, bot_first, bot_second, bot_third]

table = Table()
table.first_draw(players)

table.bet(player, 8)
table.bet(bot_first, 3)
table.bet(bot_second, 5)
table.bet(bot_third, 12)

for player in players:
    print(player)

print(table.get_cards())