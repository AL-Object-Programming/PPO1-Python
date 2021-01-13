import random


class Dice:
    sides: int

    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        result = random.randint(1, self.sides)
        print("Dice roll: " + str(result))
        return result
