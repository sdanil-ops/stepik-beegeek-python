#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    program for displaying three consecutive numbers on the screen,
#    each on a separate line. The first number is entered by the user,
#    the rest of the numbers are calculated in the program.
#    -----------------------------------------------------------
from task1 import TestUnit

class Number:
    def __init__(self, value: int):
        self.value = value
        self.next = self.get_next(self.value)
        self.one_after_next = self.get_next(self.next)
        self.sequence = self.__repr__()

    def get_next(self, value: int):
        return value + 1


    def __repr__(self):
        return f'{self.value}\n{self.next}\n{self.one_after_next}'


#---------- test -----------
# if __name__ == '__main__':
#     test = TestUnit(Number, 1, '1\n2\n3')
#     print('passed' if test.is_passed else 'failed')


#---------- run ------------
if __name__ == '__main__':
    number = Number(int(input()))
    print(number.sequence)