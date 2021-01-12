from board import Board
from dice import Dice
from pawn import Pawn

if __name__ == '__main__':
    board = Board()
    board.dice = Dice()
    board.pawns.append(Pawn("Luke Skywalker"))
    board.pawns.append(Pawn("Darth Vader"))

    try:
        while True:
            board.preform_turn()
    except:
        print(" ")
        print(board.winner.name + " won.")
