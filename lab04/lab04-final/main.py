import random

from board import Board
from dice import Dice
from pawn import Pawn

if __name__ == '__main__':
    names = ['Liam', 'Olivia', 'Noah', 'Emma', 'Oliver', 'Ava', 'William', 'Sophia', 'Elijah', 'Isabella']
    number_of_players = random.randint(2, 9)
    max_turn = 999

    while True:
        print(' ')
        print('Do you want to specify max turn? y/n')
        answer = input()
        if answer == 'y':
            print('Enter max turn')
            max_turn = input()
        if answer == 'n':
            break

    print(" ")
    print("Enter max position in game: ")
    max_position = int(input())
    board = Board(max_position, max_turn)

    print(" ")
    sides: int
    print("Enter number of dice\'s sides")
    sides = int(input())

    board.dice = Dice(sides)

    for index in range(number_of_players):
        board.pawns.append(Pawn(names[index]))

    try:
        while True:
            board.preform_turn()
    except:
        print(" ")
        print(board.winner.name + " won.")
