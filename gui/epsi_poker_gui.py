import tkinter as tk
import gui.game_mode_page as gmp
import gui.solo_game_page as sgp
import gui.start_page as sp
import gui.parameters_page as pp
import gui.color as c


class EpsiPokerGui(tk.Tk):

    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (sp.StartPage, pp.ParametersPage, gmp.GameModePage, sgp.SoloGamePage):
            frame = F(container, self)

            # initializing frame of that object from
            # Startpage, ParametersPage, GameModePage, SoloPartPage respectively with
            # for loop
            self.frames[F] = frame

            frame.configure(background=c.Color.PURPLE.value)
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(sp.StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


if __name__ == "__main__":
    # create the application
    epsi_poker_gui = EpsiPokerGui()
    epsi_poker_gui.mainloop()
