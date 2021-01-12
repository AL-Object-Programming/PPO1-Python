from point import Point


class Square:
    a: Point
    b: Point
    c: Point
    d: Point

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def show(self):
        return print("a: " + str(self.a.show()) + " "
                     "b: " + str(self.b.show()) + " "
                     "c: " + str(self.c.show()) + " "
                     "d: " + str(self.d.show()))
