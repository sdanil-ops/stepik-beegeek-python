#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    The program receives three lines as input, each on a separate line.
#    The program should output the entered lines in the same sequence,
#    each on a separate line.
#    -----------------------------------------------------------
from typing import List
from task1 import TestUnit


class ThreeStrings:
    def __init__(self, strings: List[str]):
        self.strings = strings

    def __repr__(self):
        result = ''
        for string in self.strings:
            result += string + '\n'

        return result

# test
if __name__ == '__main__':
    test = TestUnit(ThreeStrings, ['i', 'was', 'born'], 'i\nwas\nborn\n')
    print('passed' if test.is_passed else 'failed')

# run
# if __name__ == '__main__':
#     strings = ThreeStrings([input() for _ in range(3)])
#     print(strings)