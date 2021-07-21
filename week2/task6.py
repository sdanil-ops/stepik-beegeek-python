#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    The input to the program is a line of text - the name of
#    the football team. The program repeats it on the screen
#    with the words "- чемпион!" Uses similar to task1 code.
#    -----------------------------------------------------------
class TeamChampion:
    def __init__(self, name: str):
        self.name = name

    def praise(self):
        return f'{self.name} - чемпион!'

    def __str__(self):
        return f'{self.name} - чемпион!'


class TestUnit:
    def __init__(self, _class, _input, _output):
        self._class = _class
        self._input = _input
        self._output = _output
        self.is_passed = self.is_passed_test()
        print('testing...', self._class)

    def is_passed_test(self):
        test = self._class(self._input)
        return test.praise() == self._output


if __name__ == '__main__':
    team = TeamChampion(input())
    print(team)

# if __name__ == '__main__':
#     test = TestUnit(TeamChampion, 'Барселона', 'Барселона - чемпион!')
#     print('passed' if test.is_passed else 'failed')
