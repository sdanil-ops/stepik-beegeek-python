#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Program reads two integers a and b and displays
#    the square of the sum and the sum of squares
#    -----------------------------------------------------------
from typing import Tuple


def calculate_squared_sum(a: int, b: int) -> int:
    """returns squared sum of a and b"""
    return (a + b) ** 2


def calculate_sum_of_squares(a: int, b: int) -> int:
    """returns sum of square sum of a and b"""
    return (a ** 2) + (b ** 2)


def get_square_sum_sum_of_squares(a: int, b: int) -> Tuple[str, str]:
    return f'Квадрат суммы {a} и {b} равен {calculate_squared_sum(a, b)}', \
           f'Сумма квадратов {a} и {b} равна {calculate_sum_of_squares(a, b)}'


if __name__ == '__main__':
    print(*get_square_sum_sum_of_squares(int(input()), int(input())), sep='\n')
