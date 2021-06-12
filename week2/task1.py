#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#
#    displays  "Hello, world!". You can paste any name against 'world'
#    -----------------------------------------------------------
from typing import Optional

class HelloMessage:
    def __init__(self, recipient: str = None):
        if recipient is not None:
            self.recipient = recipient
        else:
            self.recipient = 'мир'

    def __str__(self):
        return f'Здравствуй, {self.recipient}!'


class TestUnit:
    def __init__(self, _class, _input, _output):
        self._class = _class
        self._input = _input
        self._output = _output
        self.is_passed = self.is_passed_test()
        print('testing...', self._class, end=' ')

    def is_passed_test(self):
        test = self._class(self._input)
        return test.__str__() == self._output


def test_hello_message(test: Optional[str] = None):
    print('testing...', test)
    test_case_passed = HelloMessage(test).__str__() == f'Здравствуй, {test}!' if test else 'Здравствуй, Мир!'
    print('passed' if test_case_passed else 'fail')


if __name__ == '__main__':
    test = TestUnit(HelloMessage, 'Гвидо', 'Здравствуй, Гвидо!')
    print('passed' if test.is_passed else 'fail')
