#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    The program is fed three lines, each on a separate line.
#    The program should print the entered lines in reverse order,
#    each on a separate line. Uses code from previous task.
#    Just paste it.
#    -----------------------------------------------------------
from task7 import get_list_from_input


def print_reverted_list(data: list):
    """Prints unpacked list in reverse order. Each element on separate line"""
    print(*data[::-1], sep='\n')


print_reverted_list(get_list_from_input())
