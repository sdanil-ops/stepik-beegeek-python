#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that determines whether the king can get
#    from the first square (x) to the second (y) in one move.
#    -----------------------------------------------------------
from typing import Tuple


def is_king_move(x: Tuple[int, int], y: Tuple[int, int]) -> bool:
    """returns True if king can move from x to y"""
    return -1 <= x[0] - y[0] <= 1 and -1 <= x[1] - y[1] <= 1


def check_king_move(x: Tuple[int, int], y: Tuple[int, int]) -> str:
    if is_king_move(x, y):
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    print(check_king_move((int(input()), int(input())), (int(input()), int(input()))))
