import random


class Dice:
    def roll(self):
        result = random.randint(0, 6)
        print("Dice roll: " + str(result))
        return result
