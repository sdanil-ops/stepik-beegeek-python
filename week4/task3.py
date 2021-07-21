#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that checks that for a given four-digit number,
#    the following relationship holds: the sum of the first and
#    last digits is equal to the difference between the second
#    and third digits.
#    -----------------------------------------------------------
class Number:
    def __init__(self, value: int):
        self.value = value
        self.sum_of_first_and_last_digits = self.calculate_sum_of_first_and_last_digits()
        self.difference_between_second_and_third_digits = self.calculate_difference_between_second_and_third_digits()
        self.ratio = self.check_ratio()

    def calculate_sum_of_first_and_last_digits(self):
        return (self.value % 10) + ((self.value % 10 ** 4) // 10 ** 3)

    def calculate_difference_between_second_and_third_digits(self):
        return ((self.value % 10 ** 3) // 10 ** 2) - (self.value % 10 ** 2) // 10 ** 1

    def check_ratio(self):
        if self.sum_of_first_and_last_digits == self.difference_between_second_and_third_digits:
            return 'ДА'
        return 'НЕТ'


# ----------- testing -----------
# if __name__ == '__main__':
#     test_is_passed = Number(1614).ratio == 'ДА'
#     print('test 1 passed' if test_is_passed else 'failed test 1')
#     test_is_passed = Number(1234).ratio == 'НЕТ'
#     print('test 2 passed' if test_is_passed else 'failed test 2')
#     test_is_passed = Number(7911).ratio == 'ДА'
#     print('test 3 passed' if test_is_passed else 'failed test 3')

# ----------- running -----------
if __name__ == '__main__':
    number = Number(int(input()))
    print(number.ratio)
