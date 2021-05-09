#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    program for displaying three consecutive numbers on the screen,
#    each on a separate line. The first number is entered by the user,
#    the rest of the numbers are calculated in the program.
#    -----------------------------------------------------------
def print_consecutive_numbers(number: int = None, quantity: int = 3):
    """Prints sequence of consecutive numbers with specified quantity"""
    if number is None:
        number = int(input())
    for i in range(quantity):
        print(number + i)


print_consecutive_numbers()