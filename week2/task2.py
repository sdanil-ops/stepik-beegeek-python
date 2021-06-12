#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that prints a sequence of numbers
#    with one space between them. Sequence is '4 8 15 16 23 42'
#    You can use any sequence to print
#    -----------------------------------------------------------
class Sequence:
    def __init__(self, data: list):
        self.data = data

    def __str__(self):
        return ' '.join(self.data)


class TestUnit:
    def __init__(self, _class, _input, _output):
        self._class = _class
        self._input = _input
        self._output = _output
        self.is_passed = self.is_passed_test()
        print('test...', end=' ')

    def is_passed_test(self):
        test_case = self._class(self._input)
        return test_case.__str__() == self._output


if __name__ == '__main__':
    test = TestUnit(Sequence, ['4', '8', '15', '16', '23', '42'], '4 8 15 16 23 42')
    print('passed' if test.is_passed else 'failed')
