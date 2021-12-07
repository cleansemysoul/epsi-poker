import os
import random
import tkinter as tk
from PIL import Image, ImageTk
import gui.game_mode_page as gmp
import model.solo_game as sg
import gui.color as gc
import model.card as mc
import logging
logging.basicConfig(level=logging.INFO)


class SoloGamePage(tk.Frame):
    """ represent solo game gui """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.solo_game = None
        self.image_list = None
        self.controller = controller

        # launch game button
        self.btn_launch_gane = tk.Button(self, text="Lancer la partie solo", height=40, width=80)
        self.btn_launch_gane.configure(background=gc.Color.YELLOW.value)
        self.btn_launch_gane.configure(foreground=gc.Color.BLACK.value)
        self.btn_launch_gane.configure(command=self.launch_gane)
        self.btn_launch_gane.grid(row=9, column=1)

    def launch_gane(self):

        # delete launch game button
        self.btn_launch_gane.destroy()

        # get the seed
        seed = random.randrange(0, 1000) if self.controller.seed.get() == "" else int(self.controller.seed.get())

        # new solo game
        self.solo_game = sg.SoloGame(seed)

        # for storing those images
        self.image_list = []

        # display the human name
        human_label = tk.Label(self, text=self.solo_game.human_player.name)
        human_label.configure(background=gc.Color.PURPLE.value)
        human_label.configure(foreground=gc.Color.WHITE.value)
        human_label.grid(row=7, column=5, columnspan=5)

        # display the human picture
        self.display_image('human', 6, 7, "default", 100, 100)

        # display the human hand
        for card_index, card in enumerate(self.solo_game.human_player.hand.cards):
            image_name = self.get_image_name(card.color, card.value)
            human_row = 8
            human_column = 5 + card_index
            self.display_image('cards', human_row, human_column, image_name, 100, 152)

        # display the artificial intelligence hands
        ai_players = self.solo_game.ai_players

        for player_index, ai_player in enumerate(ai_players):
            for card_index, card in enumerate(ai_player.hand.cards):
                # image_name = self.get_image_name(card.color, card.value)
                image_name = "default"
                grid = [
                    {"row": 5, "column": 0 + card_index},
                    {"row": 2, "column": 5 + card_index},
                    {"row": 5, "column": 10 + card_index}
                ]
                self.display_image('cards', grid[player_index]["row"], grid[player_index]["column"], image_name, 100, 152)

        # display the artificial intelligence name
        grid = [{"row": 4, "column": 0},{"row": 1, "column": 5}, {"row": 4, "column": 10}]
        for player_index, ai_player in enumerate(ai_players):
            ai_label = tk.Label(self, text=ai_player.name)
            ai_label.configure(background=gc.Color.PURPLE.value)
            ai_label.configure(foreground=gc.Color.WHITE.value)
            ai_label.grid(row=grid[player_index]["row"], column=grid[player_index]["column"], columnspan=5)

        # display the artificial intelligence picture
        grid = [{"row": 3, "column": 2},{"row": 0, "column": 7}, {"row": 3, "column": 12}]
        for player_index, ai_player in enumerate(ai_players):
            image_name = ai_player.name
            self.display_image('ai', grid[player_index]["row"], grid[player_index]["column"], image_name, 100, 100)

        # relaunch game button
        btn_relaunch_game = tk.Button(self, text="Nouvelle partie")
        btn_relaunch_game.configure(background=gc.Color.YELLOW.value)
        btn_relaunch_game.configure(foreground=gc.Color.BLACK.value)
        btn_relaunch_game.configure(command=self.launch_gane)
        btn_relaunch_game.grid(row=9, column=0, columnspan=5, sticky='ew')

        # display the seed
        seed_label = tk.Label(self, text="Graine du jeu : {}".format(seed))
        seed_label.configure(background=gc.Color.PURPLE.value)
        seed_label.configure(foreground=gc.Color.WHITE.value)
        seed_label.grid(row=9, column=5, columnspan=5, sticky='ew')

        # quit button
        btn_stop = tk.Button(self, text="Quitter la partie")
        btn_stop.configure(background=gc.Color.YELLOW.value)
        btn_stop.configure(foreground=gc.Color.BLACK.value)
        btn_stop.configure(command=lambda: self.controller.show_frame(gmp.GameModePage))
        btn_stop.grid(row=9, column=10, columnspan=5, sticky='ew')

    @staticmethod
    def get_image_name(card_color, card_value):
        color = mc.Card.COLOR_NAME[card_color]
        value = mc.Card.VALUE_NAME[card_value]
        image_name = color + value
        return image_name

    def display_image(self, image_rep, row, column, image_name, width, height):
        scriptDir = os.path.dirname(__file__)
        impath = os.path.join(scriptDir, f'../images/{image_rep}/{image_name}.png')
        image = Image.open(str(impath))
        image = image.resize((width, height), Image.ANTIALIAS)
        photo_image = ImageTk.PhotoImage(image)
        self.image_list.append(photo_image)  # save the reference of the image

        canvas = tk.Canvas(self, width=image.size[0], height=image.size[1])
        canvas.configure(background=gc.Color.PURPLE.value)
        canvas.configure(highlightthickness=0, relief='ridge')
        canvas.create_image(0, 0, anchor=tk.NW, image=photo_image)
        canvas.grid(row=row, column=column)
