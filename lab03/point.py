class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def show(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
