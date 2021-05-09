#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    program calculates the sum, difference and product
#    of two integers entered from the keyboard.
#    -----------------------------------------------------------
def calculate_sum(a: int, b: int) -> int:
    """calculates sum of a and b"""
    return a + b


def calculate_difference(a: int, b: int) -> int:
    """calculates difference between a and b"""
    return a - b


def calculate_product(a: int, b: int) -> int:
    """calculates product of a and b"""
    return a * b


def print_sum_diff_and_prod(a: int, b: int):
    """prints sum, difference and product of a and b"""
    print(f'{a} + {b} = {calculate_sum(a, b)}')
    print(f'{a} - {b} = {calculate_difference(a, b)}')
    print(f'{a} * {b} = {calculate_product(a, b)}')


print_sum_diff_and_prod(int(input()), int(input()))
