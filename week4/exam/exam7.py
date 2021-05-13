#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that determines whether the bishop can get
#    from the first square (x) to the second (y) in one move.
#    -----------------------------------------------------------
from typing import Tuple


def is_knight_move(x: Tuple[int, int], y: Tuple[int, int]) -> bool:
    return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 == 5


def check_knight_move(x: Tuple[int, int], y: Tuple[int, int]) -> str:
    if is_knight_move(x, y):
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    print(check_knight_move((int(input()), int(input())), (int(input()), int(input()))))
