#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that prints a sequence of numbers
#    with one space between them. Sequence is '4 8 15 16 23 42'
#    You can use any sequence to print
#    -----------------------------------------------------------


def print_sequence(sequence: list = None):
    """Prints sequence of numbers with one space between them"""
    if sequence is None:
        sequence = ['4', '8', '15', '16', '23', '42']
    for element in sequence:
        print(element, end=' ')


print_sequence()
