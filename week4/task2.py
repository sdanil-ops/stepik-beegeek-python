#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that determines whether a number is odd or even.
#    -----------------------------------------------------------
class Number:
    def __init__(self, value: int):
        self.value = value
        self.is_even = self.is_even()

    def is_even(self):
        return self.value % 2 == 0

    def __str__(self):
        if self.is_even:
            return 'Четное'
        return 'Нечетное'


# ------------ testing ------------
# if __name__ == '__main__':
#     test_is_passed = Number(1).__str__() == 'Нечетное'
#     print('test 1 is passed' if test_is_passed else 'failed test 1')
#     test_is_passed = Number(2).__str__() == 'Четное'
#     print('test 2 is passed' if test_is_passed else 'failed test 2')

# ------------ running ------------
if __name__ == '__main__':
    number = Number(int(input()))
    print(number)
