import tkinter as tk
import gui.start_page as sp
import gui.color as c


class ParametersPage(tk.Frame):
    """ represent parameters page """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # seed input with label
        label_seed = tk.Label(self, text="Graine pour la génération du jeux")
        label_seed.configure(background=c.Color.PURPLE.value, foreground=c.Color.WHITE.value)
        label_seed.grid(column=1, row=0)
        self.seed = tk.StringVar(None)
        entry_seed = tk.Entry(self, textvariable=self.seed)
        entry_seed.grid(column=2, row=0)

        # back button
        btn_back = tk.Button(self, text="Retour", command=lambda: controller.show_frame(sp.StartPage))
        btn_back.grid(column=1, row=1, sticky='ew')

    def get_seed(self) -> int:
        return int(self.seed.get())
