#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that determines whether a number is odd or even.
#    -----------------------------------------------------------
def is_even(number: int) -> bool:
    """returns True if inputted number is even, else False"""
    return number % 2 == 0


def check_parity(number: int) -> str:
    """returns number parity"""
    if is_even(number):
        return 'Четное'
    return 'Нечетное'


if __name__ == '__main__':
    print(check_parity(int(input())))