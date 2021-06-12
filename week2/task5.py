#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    The program receives one line as input - name.
#    Output must be "Привет, $name". Uses similar with task 1 code.
#    to complete task remove
#    -----------------------------------------------------------
from task1 import HelloMessage
from task1 import TestUnit

if __name__ == '__main__':
    test = TestUnit(HelloMessage, 'Гвидо', 'Здравствуй, Гвидо!')
    print('passed' if test.is_passed else 'fail')



