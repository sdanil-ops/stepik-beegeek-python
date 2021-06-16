#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Input is an integer, output is previous and next integer
#    -----------------------------------------------------------
from task1 import TestUnit


class Number:
    def __init__(self, value: int):
        self.value = value
        self.next = self.get_next()
        self.prev = self.get_prev()

    def get_next(self) -> int:
        """returns next number"""
        return self.value + 1

    def get_prev(self) -> int:
        """returns previous number"""
        return self.value - 1

    def __repr__(self):
        return f'Следующее за числом {self.value} число: {self.next}\n' \
               f'Для числа {self.value} предыдущее число: {self.prev}'


# -------------- test ----------------
# if __name__ == '__main__':
#     test = TestUnit(Number, 2, f'Следующее за числом 2 число: 3\nДля числа 2 предыдущее число: 1')
#     print('passed' if test.is_passed else 'failed')


# -------------- run -----------------
if __name__ == '__main__':
    number = Number(int(input()))
    print(number)