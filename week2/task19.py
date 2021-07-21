#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    The program receives three integers as input: a1, d and n
#    Program should output  the nth term of the arithmetic progression.
#    -----------------------------------------------------------
from task1 import TestUnit


class ArithmeticProgression:
    def __init__(self, first: int, step: int):
        self.first = first
        self.step = step

    def get_n_term(self, n: int) -> int:
        return self.first + self.step * (n - 1)


# ----------- testing --------------
# if __name__ == '__main__':
#     test_data = ArithmeticProgression(1, 1)
#     test = TestUnit(test_data.get_n_term, 10, '10')
#     print('passed' if test.is_passed else 'failed')


# ----------- running ---------------
if __name__ == '__main__':
    term = ArithmeticProgression(int(input()), int(input())).get_n_term(int(input()))
    print(term)