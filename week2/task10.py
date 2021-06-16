#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    a program reads a separator string and three lines,
#    and then prints the specified lines through the separator.
#    Uses code from task7. Just paste it
#    -----------------------------------------------------------
from typing import List
from task1 import TestUnit


class StringsWithSeparator:
    def __init__(self, strings: List[str], separator: str = None):
        self.strings = strings
        if separator is None:
            self.separator = '***'
        else:
            self.separator = separator

    def separate(self):
        result = ''
        for string in self.strings:
            result += string + self.separator

        return result[:-len(self.separator)]

    def __repr__(self):
        return self.separate()


# -------------- run --------------------
if __name__ == '__main__':
    test = TestUnit(StringsWithSeparator, ['one', 'two three', 'four'], 'one***two three***four')
    print('passed' if test.is_passed else 'failed')


# ------------- test --------------------
# if __name__ == '__main__':
#     strings = StringsWithSeparator(separator=input(), strings=[input() for _ in range(3)])
#     print(strings)
