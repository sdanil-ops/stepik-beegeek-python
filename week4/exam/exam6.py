#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that determines whether the bishop can get
#    from the first square (x) to the second (y) in one move.
#    -----------------------------------------------------------
from typing import Tuple


def is_bishop_move(x: Tuple[int, int], y: Tuple[int, int]) -> bool:
    return (x[0] - x[1] == y[0] - y[1]) or (x[0] + x[1] == y[0] + y[1])


def check_bishop_move(x: Tuple[int, int], y: Tuple[int, int]) -> str:
    if is_bishop_move(x, y):
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    print(check_bishop_move((int(input()), int(input())), (int(input()), int(input()))))
