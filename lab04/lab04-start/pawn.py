class Pawn:
    position: int
    name: str

    def __init__(self, name):
        self.position = 0
        self.name = name
        print(self.name + " joined the game.")
