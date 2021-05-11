#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that takes an integer xxx and determines
#    whether the given number belongs to the specified ranges.
#    -----------------------------------------------------------
from typing import Tuple


def is_in_interval(number: int, intervals: Tuple[int, int] = (-1, 17)):
    return intervals[0] < number < intervals[1]


def check_affiliation(number: int) -> str:
    if is_in_interval(number):
        return 'Не принадлежит'
    return 'Принадлежит'


if __name__ == '__main__':
    print(check_affiliation(int(input())))
