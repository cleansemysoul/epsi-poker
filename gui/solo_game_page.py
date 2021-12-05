import logging
import os
import tkinter as tk
from PIL import Image, ImageTk
import gui.game_mode_page as gmp
import model.solo_game as sg
import gui.parameters_page as pp
import gui.color as gc
import model.card as mc
import logging
logging.basicConfig(level=logging.INFO)


class SoloGamePage(tk.Frame):
    """ represent solo game gui """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # get the seed
        seed = pp.ParametersPage.get_seed
        logging.info("Game seed: {}".format(seed))

        # new solo game
        self.solo_game = sg.SoloGame(seed)

        # for storing those images
        self.image_list = []

        # display the human hand
        for card_index, card in enumerate(self.solo_game.human_player.hand.cards):
            image_name = self.get_image_name(card.color, card.value)
            human_row = 8
            human_column = 5 + card_index
            self.display_image('cards', human_row, human_column, image_name, 150, 229)

        # display the human name
        human_label = tk.Label(self, text=self.solo_game.human_player.name)
        human_label.configure(background=gc.Color.PURPLE.value)
        human_label.configure(foreground=gc.Color.WHITE.value)
        human_label.grid(row=7, column=5, columnspan=5)

        # display the human picture
        self.display_image('human', 6, 7, "default", 100, 100)

        # display the artificial intelligence hands
        ai_players = self.solo_game.ai_players
        for player_index, ai_player in enumerate(ai_players):
            for card_index, card in enumerate(ai_player.hand.cards):
                # image_name = self.get_image_name(card.color, card.value)
                image_name = "default"
                ai_row = 0
                ai_column = 0
                if player_index == 0:
                    ai_row = 5
                    ai_column = 0 + card_index
                elif player_index == 1:
                    ai_row = 2
                    ai_column = 5 + card_index
                elif player_index == 2:
                    ai_row = 5
                    ai_column = 10 + card_index
                self.display_image('cards', ai_row, ai_column, image_name, 150, 229)

        # display the artificial intelligence name
        for player_index, ai_player in enumerate(ai_players):
            ai_row = 0
            ai_column = 0
            if player_index == 0:
                ai_row = 4
                ai_column = 0
            elif player_index == 1:
                ai_row = 1
                ai_column = 5
            elif player_index == 2:
                ai_row = 4
                ai_column = 10
            ai_label = tk.Label(self, text=ai_player.name)
            ai_label.configure(background=gc.Color.PURPLE.value)
            ai_label.configure(foreground=gc.Color.WHITE.value)
            ai_label.grid(row=ai_row, column=ai_column, columnspan=5)

        # display the artificial intelligence picture
        for player_index, ai_player in enumerate(ai_players):
            image_name = ai_player.name
            ai_row = 0
            ai_column = 0
            if player_index == 0:
                ai_row = 3
                ai_column = 2
            elif player_index == 1:
                ai_row = 0
                ai_column = 7
            elif player_index == 2:
                ai_row = 3
                ai_column = 12
            self.display_image('ai', ai_row, ai_column, image_name, 100, 100)

        # quit button
        btn_stop = tk.Button(self, text="Quitter la partie", command=lambda: controller.show_frame(gmp.GameModePage))
        btn_stop.grid(row=9, column=0, columnspan=15)

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
