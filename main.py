# TODO : Erwann déconseille l’import from … import …
from model.player import Player
from model.table import Table


def main():
    player = Player("Human")
    bot_first = Player("IA 1")
    bot_second = Player("IA 2")
    bot_third = Player("IA 3")

    players = [player, bot_first, bot_second, bot_third]

    table = Table(10)
    table.first_draw(players)

    table.bet(player, 8)
    table.bet(bot_first, 3)
    table.bet(bot_second, 5)
    table.bet(bot_third, 12)

    for player in players:
        print(player)

    print(table.get_cards())


if __name__ == "__main__":
    main()
