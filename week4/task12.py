#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that takes an integer xxx and determines
#    whether the given number belongs to the specified ranges.
#    -----------------------------------------------------------
from typing import Tuple


class Interval:
    area: Tuple[Tuple[int, int], Tuple[int, int]] or Tuple[int, int]


class Point(Interval):
    def __init__(self, point: int):
        self.point = point
        self.in_interval = self.is_in_interval()
        self.affiliation = self.check_affiliation()

    def is_in_interval(self):
        return self.area[0][0] < self.point < self.area[0][1] or self.area[1][0] < self.point < self.area[1][1]

    def check_affiliation(self):
        if self.in_interval:
            return 'Принадлежит'
        return 'Не принадлежит'


if __name__ == '__main__':
    Interval.area = ((-30, -1), (7, 26))
    # ------------ testing ------------
    # tests = {
    #     'test 1': Point(-332).in_interval != True,
    #     'test 2': Point(-30).in_interval != True,
    #     'test 3': Point(-21).in_interval is True
    # }
    # for test in tests:
    #     print(f'passed {test}' if tests[test] else f'failed {test}')
    # ------------ running ------------
    point = Point(int(input()))
    print(point.affiliation)
