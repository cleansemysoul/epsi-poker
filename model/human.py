import model.player as p


class Human(p.Player):
    """ represent human player """

    def __init__(self, name, chips=50):
        super().__init__(name, chips)

    def __str__(self) -> str:
        return f"Type: Human, Name : {self.name}, Chip : {self.chips}"
