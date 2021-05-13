#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that determines whether the queen can get
#    from the first square (x) to the second (y) in one move.
#    -----------------------------------------------------------
from typing import Tuple


def is_queen_move(x: Tuple[int, int], y: Tuple[int, int]) -> bool:
    first = x[0] - y[0]
    second = x[1] - y[1]
    return abs(first) == abs(second) or (first == 0 or second == 0)


def check_queen_move(x: Tuple[int, int], y: Tuple[int, int]) -> str:
    if is_queen_move(x, y):
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    print(check_queen_move((int(input()), int(input())), (int(input()), int(input()))))
