#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    a program for finding the digits of a four-digit number
#    -----------------------------------------------------------
class Number:
    def __init__(self, value: int):
        self.value = value
        self.ones = self.count_ones()
        self.tens = self.count_tens()
        self.hundreds = self.count_hundreds()
        self.thousands = self.count_thousands()

    def count_ones(self) -> int:
        return self.value % 10

    def count_tens(self):
        return (self.value // 10) % 10

    def count_hundreds(self):
        return (self.value // 100) % 10

    def count_thousands(self):
        return self.value // 1000

    def __repr__(self):
        return f'Цифра в позиции тысяч равна {self.thousands}\nЦифра в позиции сотен равна {self.hundreds}\nЦифра в ' \
               f'позиции десятков равна {self.tens}\nЦифра в позиции единиц равна {self.ones} '

# ------------- testing -------------
# if __name__ == '__main__':
#     test_is_passed = Number(3281).thousands == 3
#     print('passed' if test_is_passed else 'failed')
#     test_is_passed = Number(3281).hundreds == 2
#     print('passed' if test_is_passed else 'failed')
#     test_is_passed = Number(3281).tens == 8
#     print('passed' if test_is_passed else 'failed')
#     test_is_passed = Number(3281).ones == 1
#     print('passed' if test_is_passed else 'failed')
# ------------- running -------------
if __name__ == '__main__':
    number = Number(int(input()))
    print(number)