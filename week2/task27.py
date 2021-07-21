#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    program calculates the sum and the product
#    of the digits of a positive three-digit number.
#    -----------------------------------------------------------
from task1 import TestUnit


class Number:
    def __init__(self, value: int):
        self.value = value
        self.sum_of_digits = self.calculate_sum_of_digits(self.value)
        self.product_of_digits = self.calculate_product_of_digits(self.value)

    def calculate_sum_of_digits(self, number: int) -> int:
        result = 0
        while number > 0:
            result += number % 10
            number //= 10
        return result

    def calculate_product_of_digits(self, number: int):
        result = 1
        while number > 0:
            result *= number % 10
            number //= 10
        return result

    def __repr__(self):
        return f'Сумма цифр = {self.sum_of_digits}\nПроизведение цифр = {self.product_of_digits}'


# ------------ testing ------------
if __name__ == '__main__':
    test = TestUnit(Number, 123, 'Сумма цифр = 6\nПроизведение цифр = 6')
    print('passed' if test.is_passed else 'failed')


# ------------ running ------------
# if __name__ == '__main__':
#     number = Number(int(input()))
#     print(number)
