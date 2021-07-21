#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    program that calculates the cost of three computers,
#    consisting of a monitor, system unit, keyboard and mouse.
#
#    -----------------------------------------------------------
from typing import List
from task1 import TestUnit


class PCSet:
    def __init__(self, prices: List[int]):
        self.prices = prices
        self.total = self.calculate_total()

    def calculate_total(self):
        result = 0
        for price in self.prices:
            result += price
        return result


class PCSetCost(PCSet):
    def __str__(self):
        return self.total


# ------------ testing --------------
# if __name__ == '__main__':
#     test = TestUnit(PCSetCost, [1, 2, 3, 4], 10)
#     print('passed' if test.is_passed else 'failed')


# ------------ running --------------
if __name__ == '__main__':
    pc_set_cost = PCSetCost([int(input()) for _ in range(4)])
    print(pc_set_cost.total * 3)
