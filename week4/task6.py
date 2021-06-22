#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that determines the smallest of two numbers
#    -----------------------------------------------------------
class TwoNumbers:
    def __init__(self, number: int, number_: int):
        self.number = number
        self.number_ = number_
        self.lesser = self.get_lesser()

    def is_lesser(self):
        return self.number < self.number_

    def get_lesser(self):
        if self.is_lesser():
            return self.number
        return self.number_


# ------------ testing ------------
# if __name__ == '__main__':
#     tests = {
#         'test 1': TwoNumbers(8, 11).lesser == 8,
#         'test 2': TwoNumbers(20, 5).lesser == 5,
#         'test 3': TwoNumbers(-1, 1).lesser == -1,
#         'test 4': TwoNumbers(0, 0).lesser == 0,
#         'test 5': TwoNumbers(1, 10000).lesser == 1
#     }
#     for test in tests:
#         print(f'passed {test}' if tests[test] else f'failed {test}')

# ------------ running ------------
if __name__ == '__main__':
    two_numbers = TwoNumbers(int(input()), int(input()))
    print(two_numbers.lesser)
