import model.player as p


class Ai(p.Player):
    """ represent artificial intelligence player """

    def __init__(self, name, chips=50):
        super().__init__(name, chips)

    def __str__(self) -> str:
        return f"Type: artificial intelligence, Name : {self.name}, Chip : {self.chips}"
