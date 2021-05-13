#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that determines whether the rook can get
#    from the first square (x) to the second (y) in one move.
#    -----------------------------------------------------------
from typing import Tuple


def is_rook_move(x: Tuple[int, int], y: Tuple[int, int]) -> bool:
    """returns True if rook can move from x to y """
    return x[0] == y[0] or x[1] == y[1]


def check_rook_move(x: Tuple[int, int], y: Tuple[int, int]) -> str:
    if is_rook_move(x, y):
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    print(check_rook_move((int(input()), int(input())), (int(input()), int(input()))))
