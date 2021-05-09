#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Modify the previous program so that each number
#    in the sequence is printed on a separate line.
#    -----------------------------------------------------------

def print_sequence(sequence: list = None):
    """Prints sequence of numbers each one on separate line"""
    if sequence is None:
        sequence = ['4', '8', '15', '16', '23', '42']
    for element in sequence:
        print(element)


print_sequence()