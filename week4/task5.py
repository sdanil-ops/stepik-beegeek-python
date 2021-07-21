#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that determines whether three given numbers
#    are consecutive members of an arithmetic progression.
#    -----------------------------------------------------------
from typing import List


class ArithmeticProgression:
    def __init__(self, data_list: List[int]):
        self.data_list = data_list
        self.is_valid = self.is_valid_progression()

    def is_valid_progression(self):
        return self.data_list[1] - self.data_list[0] == self.data_list[2] - self.data_list[1]

    def __call__(self):
        print('YES' if self.is_valid else 'NO')


# ------------- testing -------------
# if __name__ == '__main__':
#     test_is_passed = ArithmeticProgression([1, 2, 3]).is_valid
#     print('test 1 passed' if test_is_passed else 'test 1 is failed')
#     test_is_passed = ArithmeticProgression([1, 2, 4]).is_valid
#     print('test 2 passed' if not test_is_passed else 'test 2 is failed')
#     test_is_passed = ArithmeticProgression([2, 4, 8]).is_valid
#     print('test 3 passed' if not test_is_passed else 'test 3 is failed')

# ------------- running -------------
if __name__ == '__main__':
    is_arithmetic_progression = ArithmeticProgression([int(input()) for _ in range(3)])
    is_arithmetic_progression()
