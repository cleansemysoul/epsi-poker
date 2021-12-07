import tkinter as tk
import gui.start_page as sp
import gui.color as c
import logging
logging.basicConfig(level=logging.INFO)


class ParametersPage(tk.Frame):
    """ represent parameters page gui """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # seed input with label
        label_seed = tk.Label(self, text="Graine pour la génération du jeux")
        label_seed.configure(background=c.Color.PURPLE.value, foreground=c.Color.WHITE.value)
        label_seed.grid(column=1, row=0)
        self.entry_seed = tk.Entry(self)
        self.entry_seed.grid(column=2, row=0)

        # save button
        btn_save = tk.Button(self, text="Enregistrer", command=self.save)
        btn_save.grid(column=2, row=1, sticky='ew')

        # back button
        btn_back = tk.Button(self, text="Retour", command=lambda: controller.show_frame(sp.StartPage))
        btn_back.grid(column=1, row=1, sticky='ew')

    def save(self):
        logging.info("Save game seed: {}".format(self.entry_seed.get()))
        self.controller.seed.set(self.entry_seed.get())
