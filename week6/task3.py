#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that reads one number from the keyboard
#    and prints the inverse of it. If at the same time
#    the number entered from the keyboard is zero,
#    then output "The reverse number does not exist" (without quotes).
#    -----------------------------------------------------------
class Number:
    def __init__(self, number: float):
        self.value = number
        self.inverse = self.inverse_number(number)

    def inverse_number(self, number: float):
        try:
            return 1 / number
        except ZeroDivisionError:
            return 'Обратного числа не существует'

if __name__ == '__main__':
    number = Number(float(input()))
    print(number.inverse)
