#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    a program that greets the user by outputting the word
#    "Привет" (without quotes), followed by a comma and space,
#    followed by the name and exclamation point entered.
#    -----------------------------------------------------------
from task1 import TestUnit


class HelloMessage:
    def __init__(self, name: str = None):
        if name is None:
            self.name = 'friend'
        else:
            self.name = name

    def __repr__(self):
        return f'Привет, {self.name}!'


# _________ test ___________
if __name__ == '__main__':
    test = TestUnit(HelloMessage, 'Гвидо', 'Привет, Гвидо!')
    print('passed' if test.is_passed else 'failed')


# _________ run ____________
# if __name__ == '__main__':
#     hello_message = HelloMessage(input())
#     print(hello_message)
