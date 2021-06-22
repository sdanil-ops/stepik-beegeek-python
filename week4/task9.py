#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that reads three numbers and only sums the positive numbers.
#    -----------------------------------------------------------
from typing import List


class NumberList:
    def __init__(self, data: List[int]):
        self.data = data
        self.sum_of_positive_numbers = self.calculate_sum_of_positive_numbers()

    @staticmethod
    def is_positive(number: int) -> bool:
        return number >= 0

    def calculate_sum_of_positive_numbers(self):
        result = 0
        for number in self.data:
            if self.is_positive(number):
                result += number
        return result


if __name__ == '__main__':
    # ---------- testing ----------
    # tests = {
    #     'test 1': NumberList([4, -22, 1]).sum_of_positive_numbers == 5,
    #     'test 2': NumberList([33, 55, 63]).sum_of_positive_numbers == 151,
    #     'test 3': NumberList([-1, 37, 62]).sum_of_positive_numbers == 99,
    #     'test 4': NumberList([-1, -2, -3]).sum_of_positive_numbers == 0,
    #     'test 5': NumberList([0, 0, 0]).sum_of_positive_numbers == 0
    # }
    #
    # for test in tests:
    #     print(f'passed {test}' if tests[test] else f'failed {test}')
    # ---------- running ----------
    number_list = NumberList([int(input()) for _ in range(3)])
    print(number_list.sum_of_positive_numbers)
