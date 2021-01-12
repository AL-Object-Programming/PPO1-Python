from typing import List

from dice import Dice
from pawn import Pawn


class Board:
    max_position = 100

    pawns: List[Pawn]
    dice: Dice
    winner: Pawn
    turns_counter: int

    def __init__(self):
        self.pawns = []
        self.winner = None
        self.dice = None
        self.turns_counter = 0

    def preform_turn(self):
        self.turns_counter += 1
        print(" ")
        print("Turn " + str(self.turns_counter))
        for pawn in self.pawns:
            roll_result = self.dice.roll()
            pawn.position += roll_result
            print(pawn.name + " new position: " + str(pawn.position))

            if pawn.position >= Board.max_position:
                self.winner = pawn
                raise Exception()
