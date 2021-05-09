#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    program calculates the sum and the product
#    of the digits of a positive three-digit number.
#    -----------------------------------------------------------
from typing import Tuple


def calculate_sum_of_digits(number: int) -> int:
    """returns sum of digits of a positive number"""
    result = 0
    while number > 0:
        result += number % 10
        number //= 10
    return result


def calculate_product_of_digits(number: int) -> int:
    """returns product of digits of a positive number"""
    result = 1
    while number > 0:
        result *= number % 10
        number //= 10
    return result


def get_sum_and_product_of_digits(number: int) -> Tuple[str, str]:
    """returns sum and product of a positive number"""
    return f'Сумма цифр = {calculate_sum_of_digits(number)}', \
           f'Произведение цифр = {calculate_product_of_digits(number)}'


if __name__ == '__main__':
    print(*get_sum_and_product_of_digits(int(input())), sep='\n')
