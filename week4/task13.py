#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Let's call a number beautiful if it is four-digit and
#    divisible by 7 or 17. Write a program that determines
#    whether the entered number is beautiful. The program
#    should print "YES" if the number is pretty, or "NO" otherwise.
#    -----------------------------------------------------------
class Number:
    def __init__(self, value: int):
        self.value = value
        self.is_intresting = self.is_interesting_number()
        self.interestingness = 'YES' if self.is_intresting else 'NO'

    def is_interesting_number(self):
        return (1000 <= self.value <= 9999) and ((self.value % 7 == 0) or (self.value % 17 == 0))


if __name__ == '__main__':
    # ------------- testing -------------

    # tests = {
    #     'test 1': Number(1043).interestingness == 'YES',
    #     'test 2': Number(1045).interestingness == 'NO',
    #     'test 3': Number(2751).interestingness == 'YES'
    # }
    # for test in tests:
    #     print(f'passed {test}' if tests[test] else f'failed {test}')

    # ------------- running -------------

    number = Number(int(input()))
    print(number.interestingness)
