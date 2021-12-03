import tkinter as tk
import gui.game_mode_page as gmp


class SoloGamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # quit button
        btn_stop = tk.Button(self, text="Quitter la partie", command=lambda: controller.show_frame(gmp.GameModePage))
        btn_stop.grid(column=0, row=0)