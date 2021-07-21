#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#
#    program that displays the text "I *** like *** Python"
#    -----------------------------------------------------------
from task1 import TestUnit


class StringWithSeparator:
    def __init__(self, string: str = None, separator: str =None):
        self.string = string
        if separator is None:
            self.separator = '***'
        else:
            self.separator = separator

    def separate(self):
        return self.string.replace(' ', self.separator)

    def __repr__(self):
        return self.separate()


if __name__ == '__main__':
    string = StringWithSeparator('I like Python')
    print(string)


# if __name__ == '__main__':
#     test = TestUnit(StringWithSeparator, 'I like Python', 'I***like***Python')
#     print('passed' if test.is_passed else 'failed')
