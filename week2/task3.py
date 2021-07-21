#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that prints a sequence of numbers
#    with one space between them. Sequence is '4 8 15 16 23 42'
#    You can use any sequence to print
#    -----------------------------------------------------------
from task1 import TestUnit


class Sequence:
    def __init__(self, data: list):
        self.data = data

    def _print(self):
        for element in self.data:
            print(element, end='\n')

    def __str__(self):
        return ' '.join(self.data)


if __name__ == '__main__':
    test = TestUnit(Sequence, ['4', '8', '15', '16', '23', '42'], '4 8 15 16 23 42')
    print('\ntest passed' if test.is_passed else '\ntest failed')