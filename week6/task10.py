#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Let's call a number interesting if the difference between
#    the maximum and minimum digits in it is equal to the average
#    digit. Write a program that detects an interesting number
#    or not. If the number is interesting,
#    you should print - "The number is interesting"
#    otherwise "The number is not interesting"
#    -----------------------------------------------------------
class Number:
    def __init__(self, value: int = None):
        self.value = value
        self.is_interesting = True if self.is_interesting_number(value) else False

    def is_interesting_number(self, value: int) -> bool:
        total = (value // 100) + ((value % 100) // 10) + (value % 10)
        return (max(value // 100, (value % 100) // 10, value % 10) -
                min(value // 100, (value % 100) // 10, value % 10)) == \
               (total - min(value // 100, (value % 100) // 10, value % 10) -
                max(value // 100, (value % 100) // 10, value % 10))

    def __str__(self):
        if self.is_interesting:
            return 'Число интересное'
        return 'Число неинтересное'


if __name__ == '__main__':
    number = Number(int(input()))
    print(str(number))
