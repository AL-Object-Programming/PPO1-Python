import math
import random
from typing import List

from point import Point
from square import Square


def check_if_square(square: Square):
    ab = math.sqrt(pow((square.a.x - square.b.x), 2)) + (pow((square.a.y - square.b.y), 2))
    bc = math.sqrt(pow((square.b.x - square.c.x), 2)) + (pow((square.b.y - square.c.y), 2))
    ad = math.sqrt(pow((square.a.x - square.d.x), 2)) + (pow((square.a.y - square.d.y), 2))
    cd = math.sqrt(pow((square.c.x - square.d.x), 2)) + (pow((square.c.y - square.d.y), 2))
    if ab == bc and ab == ad and ab == cd and bc == ad and bc == cd and ad == cd:
        print("square is geometrically correct")
        return 1
    return 0


if __name__ == '__main__':
    min = 0
    max = 5
    counter = 0
    squares: List[Square] = []
    for index in range(700):
        a = Point(random.randint(min, max), random.randint(min, max))
        b = Point(random.randint(min, max), random.randint(min, max))
        c = Point(random.randint(min, max), random.randint(min, max))
        d = Point(random.randint(min, max), random.randint(min, max))
        squares.append(Square(a, b, c, d))

    for square in squares:
        square.show()
        counter += check_if_square(square)
    print("There were " + str(counter) + " geometrically correct squares.")
