#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    The program is fed three lines, each on a separate line.
#    The program should print the entered lines in reverse order,
#    each on a separate line. Uses code from previous task.
#    Just paste it.
#    -----------------------------------------------------------
from typing import List
from task1 import TestUnit


class ThreeStrings:
    def __init__(self, strings: List[str]):
        self.strings = strings

    def __repr__(self):
        data = self.strings[::-1]
        result = ''
        for string in data:
            result += string + '\n'

        return result

# test
# if __name__ == '__main__':
#     test = TestUnit(ThreeStrings, ['i', 'was', 'born'], 'i\nwas\nborn\n')
#     print('passed' if test.is_passed else 'failed')

# run
if __name__ == '__main__':
    strings = ThreeStrings([input() for _ in range(3)])
    print(strings)