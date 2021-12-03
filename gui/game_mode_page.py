import tkinter as tk
import gui.solo_game_page as sgp
import gui.start_page as sp
import gui.color as c


class GameModePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # playing solo button
        btn_play_solo = tk.Button(self, text="Jouer en solo", height=40, width=40)
        btn_play_solo.configure(background=c.Color.YELLOW.value)
        btn_play_solo.configure(foreground=c.Color.BLACK.value)
        btn_play_solo.configure(command=lambda: controller.show_frame(sgp.SoloGamePage))
        btn_play_solo.grid(column=1, row=0)

        # playing online button
        btn_play_online = tk.Button(self, text="Jouer en ligne", height=40, width=40, state='disabled')
        btn_play_online.configure(background=c.Color.YELLOW.value)
        btn_play_online.configure(foreground=c.Color.BLACK.value)
        btn_play_online.grid(column=2, row=0)

        # back button
        btn_back = tk.Button(self, text="Retour", command=lambda: controller.show_frame(sp.StartPage))
        btn_back.grid(column=1, row=1, columnspan=2, sticky='ew')