#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    There is a three-digit number abc, in which all digits are different.
#    the program displays six numbers formed by permutation of the digits of a given number.
#    -----------------------------------------------------------
from itertools import permutations


def get_list_of_digits(number: int) -> list:
    """returns list of digits of inputted number"""
    result = []
    while number != 0:
        last_digit = number % 10
        number //= 10
        result.append(last_digit)
    return result[::-1]


def _print_answer(digits_list: list):
    """crutch to print the answer in accordance with the task"""
    for i in digits_list:
        print(*i, sep='')


if __name__ == '__main__':
    _print_answer(list(permutations(get_list_of_digits(int(input())))))
