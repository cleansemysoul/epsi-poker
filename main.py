from model.player import Player
from model.table import Table
from tkinter import *
from PIL import ImageTk, Image


player = Player("Human")
bot_first = Player("IA 1")
bot_second = Player("IA 2")
bot_third = Player("IA 3")

players = [player, bot_first, bot_second, bot_third]

table = Table()
table.first_draw(players)

for player in players:
    print(player)

print(table.get_cards())


def button_click(number):
    table.bet(player, number)
    table.bet(bot_first, number)
    table.bet(bot_second, number)
    table.bet(bot_third, number)
    for player_in_game in players:
        print(player_in_game)


print(table.seed)

window = Tk()
window.title("Python Poker")
Label(window, text=f"Seed {table.seed}", fg="black", font="none 12 bold").grid(row=0, column=0, sticky=W)
for index, player in enumerate(players):
    player_cards = player.get_cards()
    Label(window, text=f"{player}", fg="black", font="none 12 bold").grid(row=index + 1, column=0, sticky=W)
    # card_picture = PhotoImage(file="cards\default0.png")
    # Label(window, image=card_picture).grid(row=index + 1, column=1, sticky=W)
    if index == 0:
        Button(window, text="Small Bet", fg="black", font="none 12 bold", command=lambda: button_click(1)).grid(row=index + 1, column=2, sticky=W)
        Button(window, text="Big Bet", fg="black", font="none 12 bold",command=lambda: button_click(5)).grid(row=index + 1, column=3, sticky=W)

Label(window, text=f"{table.get_cards()}", fg="black", font="none 12 bold").grid(row=7, column=0, sticky=W)
window.mainloop()
