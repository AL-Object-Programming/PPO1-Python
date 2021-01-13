from typing import List

from dice import Dice
from pawn import Pawn


class Board:
    max_turn: int = 999
    max_position: int
    pawns: List[Pawn]
    dice: Dice
    winner: Pawn
    turns_counter: int

    def __init__(self, max_position, max_turn):
        self.pawns = []
        self.winner = None
        self.dice = None
        self.turns_counter = 0
        self.max_position = max_position
        self.max_turn = max_turn

    def preform_turn(self):
        self.turns_counter += 1
        print(" ")
        print("Turn " + str(self.turns_counter))
        for pawn in self.pawns:
            if not (self.turns_counter == self.max_turn):
                roll_result = self.dice.roll()

                if roll_result == 1 and (pawn.position % 2) != 0:
                    print(pawn.name + " has bad luck!")
                    roll_result = self.dice.roll()
                    pawn.position -= roll_result
                    print(pawn.name + " new position: " + str(pawn.position))
                elif roll_result == self.dice.sides and (pawn.position % 7) == 0:
                    pawn.position += roll_result
                    print(pawn.name + " new position: " + str(pawn.position))
                    print(pawn.name + " has wild luck!")
                    roll_result = self.dice.roll()
                    pawn.position += roll_result
                    print(pawn.name + " new position: " + str(pawn.position))
                else:
                    pawn.position += roll_result
                    print(pawn.name + " new position: " + str(pawn.position))
                print(" ")
                if pawn.position >= self.max_position:
                    self.winner = pawn
                    raise Exception()
            else:
                self.winner = pawn
                raise Exception()
