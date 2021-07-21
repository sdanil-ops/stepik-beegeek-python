#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    program reads three integers and displays their sum.
#    Each number is written on a separate line.
#    -----------------------------------------------------------
from typing import List


class ThreeNumbers:
    def __init__(self, data: List[int]):
        self.data = data
        self.sum_of_elements = self.calculate_sum_of_elements()

    def calculate_sum_of_elements(self):
        result = 0
        for elem in self.data:
            result += elem
        return result


# ---------- test -------------
# if __name__ == '__main__':
#     print('testing...', ThreeNumbers)
#     test_is_passed = ThreeNumbers([1, 2, 3]).sum_of_elements == 6
#     print('passed' if test_is_passed else 'failed')


#----------- run --------------
if __name__ == '__main__':
    three_numbers = ThreeNumbers([int(input()) for _ in range(3)])
    print(three_numbers.sum_of_elements)