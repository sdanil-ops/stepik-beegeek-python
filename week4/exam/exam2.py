#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Two squares of a chessboard are given. Write a program
#    that determines whether the specified cells are of
#    the same color or not. If they are painted in the same
#    color, then output the word "YES", and if they have
#    different colors, then output "NO".
#    -----------------------------------------------------------
from typing import Tuple


def has_same_color(cell: Tuple[int, int], cell_: Tuple[int, int]):
    return (cell[0] + cell_[0] + cell[1] + cell_[1]) % 2 == 0


def check_cells_color(cell: Tuple[int, int], cell_: Tuple[int, int]):
    if has_same_color(cell, cell_):
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    print(check_cells_color((int(input()), int(input())), (int(input()), int(input()))))
