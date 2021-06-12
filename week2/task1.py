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


def test_hello_message(test: Optional[str] = None):
    print('testing...', test)
    test_case_passed = HelloMessage(test).__str__() == f'Здравствуй, {test}!' if test else 'Здравствуй, Мир!'
    print('passed' if test_case_passed else 'fail')


if __name__ == '__main__':
    test_hello_message('Python')
    test_hello_message('World')
    test_hello_message()
