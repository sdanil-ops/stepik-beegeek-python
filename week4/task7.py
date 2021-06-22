#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that determines the smallest of four numbers
#    -----------------------------------------------------------
from typing import List


class NumberList:
    def __init__(self, number_list: List[int]):
        self.number_list = number_list
        self.minimal_element = self.get_minimal_element(self.number_list)

    def get_minimal_element(self, number_list: list) -> int:
        if len(number_list) == 2:
            if number_list[0] < number_list[1]:
                return number_list[0]
            return number_list[1]
        result = self.get_minimal_element(number_list[1:])
        if number_list[0] < result:
            return number_list[0]
        return result


# ---------- testing ----------
# if __name__ == '__main__':
#     tests = {
#         'test 1': NumberList([1, 2, 3, 4]).minimal_element == 1,
#         'test 2': NumberList([10, 9, 11, 12]).minimal_element == 9,
#         'test 3': NumberList([100, 200, 5, 300]).minimal_element == 5,
#         'test 4': NumberList([0, 0, 0, 0]).minimal_element == 0,
#         'test 5': NumberList([1, -1, 5, 0, -5]).minimal_element == -5
#     }
#     for test in tests:
#         print(f'passed {test}' if tests[test] else f'failed {test}')

# ---------- running ----------
if __name__ == '__main__':
    number_list = NumberList([int(input()) for _ in range(4)])
    print(number_list.minimal_element)
