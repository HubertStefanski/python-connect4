import sys
import math
import numpy

_author_ = "Hubert Stefanski"


class Game:
    row_count = 4
    col_count = 4
    turn = 0

    def __init__(self, row_count=4, col_count=4, turn=0):
        self._row_count = row_count
        self._col_count = col_count
        self._turn = turn

    def get_turn(self):
        return self._turn

    def set_turn(self, x):
        self._turn = x

    def get_row_count(self):
        return self._row_count

    def set_row_count(self, x):
        self._row_count = x

    def get_col_count(self):
        return self._col_count

    def set_col_count(self, x):
        self._col_count = x


game = Game()


def create_board(r, c):
    game_board = numpy.zeros((r, c))
    return game_board


def show_author():
    print("written by : " + _author_ + "\n")


def exit_system():
    show_author()
    sys.exit("Program has been run succesfully and terminated")


def ask_for_size():
    row = int(input("Please enter the number of rows you wish to have on your board (Default min = 4, Max of 12)\n"))
    game.set_row_count(row)
    print("Number of rows entered = " + str(row) + "\n")
    col = int(input("Please enter the number of columns you wish to have on your board (default min = 4,Max of 12)\n"))
    game.set_col_count(col)
    print("Number of rows entered = " + str(col) + "\n")


def main():
    print("Welcome to connect 4 in python\n")
    ask_for_size()
    board = game.create_board(game.get_row_count(), game.get_col_count())
    print(board)
    exit_system()


main()
