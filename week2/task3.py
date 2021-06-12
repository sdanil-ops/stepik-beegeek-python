#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that prints a sequence of numbers
#    with one space between them. Sequence is '4 8 15 16 23 42'
#    You can use any sequence to print
#    -----------------------------------------------------------
class Sequence:
    def __init__(self, data: list):
        self.data = data

    def _print(self):
        for element in self.data:
            print(element, end='\n')

    def __str__(self):
        return ' '.join(self.data)



class TestUnit:
    def __init__(self, _class, _input, _output):
        self._class = _class
        self._input = _input
        self._output = _output
        self.is_passed = self.is_passed_test()
        print('testing...', end=' ')

    def is_passed_test(self):
        test = self._class(self._input)
        return test.__str__() == self._output



if __name__ == '__main__':
    sequence = Sequence(['4', '8', '15', '16', '23', '42'])
    sequence._print()