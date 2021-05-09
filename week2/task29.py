#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    a program for finding the digits of a four-digit number
#    -----------------------------------------------------------
from typing import Tuple


def count_ones(number: int) -> int:
    """returns count of ones"""
    return number % 10


def count_tens(number: int) -> int:
    """returns count of tens"""
    return (number // 10) % 10


def count_hundreds(number: int) -> int:
    """returns count of hundreds"""
    return (number // 100) % 10


def count_thousands(number: int) -> int:
    """returns count of thousands"""
    return number // 1000


def decompose_number(number: int) -> Tuple[str, str, str, str]:
    """decomposes number into components"""
    return f'Цифра в позиции тысяч равна {count_thousands(number)}', \
           f'Цифра в позиции сотен равна {count_hundreds(number)}', \
           f'Цифра в позиции десятков равна {count_tens(number)}', \
           f'Цифра в позиции единиц равна {count_ones(number)}'


if __name__ == '__main__':
    print(*decompose_number(int(input())), sep='\n')
