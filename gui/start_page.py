import tkinter as tk
import gui.game_mode_page as gmp
import gui.parameters_page as pp
import gui.color as c


class StartPage(tk.Frame):
    """represent the start page"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # configuring column sizes
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # play button
        btn_play = tk.Button(self, text="Jouer au poker EPSI", height=40, width=40)
        btn_play.configure(background=c.Color.YELLOW.value)
        btn_play.configure(foreground=c.Color.BLACK.value)
        btn_play.configure(command=lambda: controller.show_frame(gmp.GameModePage))
        btn_play.grid(column=1, row=0)

        # parameters button
        btn_param = tk.Button(self, text="Paramètres", height=40, width=40)
        btn_param.configure(background=c.Color.YELLOW.value)
        btn_param.configure(foreground=c.Color.BLACK.value)
        btn_param.configure(command=lambda: controller.show_frame(pp.ParametersPage))
        btn_param.grid(column=2, row=0)

        # quit button
        btn_quit = tk.Button(self, text="Quitter le jeu", command=self.quit)
        btn_quit.grid(column=1, row=1, columnspan=2)
