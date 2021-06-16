#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Program receives three integers as input: a1, d and n
#    Program should output  the nth term of the geometric progression.
#    -----------------------------------------------------------
from task1 import TestUnit


class GeometricProgression:
    def __init__(self, first: int, step: int):
        self.first = first
        self.step = step


class TermOfProgression(GeometricProgression):
    def get_n_term(self, n: int):
        """returns n term of geometric progression"""
        return self.first * (self.step ** (n - 1))


# ------------ testing ------------
# if __name__ == '__main__':
#     test = TestUnit(TermOfProgression(1, 2).get_n_term, 5, '16')
#     print('passed' if test.is_passed else 'failed')


# ------------ running ------------
if __name__ == '__main__':
    geometric_progression_term = TermOfProgression(int(input()), int(input())).get_n_term(int(input()))
    print(geometric_progression_term)
