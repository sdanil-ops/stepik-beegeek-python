#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that reads three numbers and only sums the positive numbers.
#    -----------------------------------------------------------
def is_positive(number: int) -> bool:
    return number >= 0


def calculate_sum_of_positives(numbers: list) -> int:
    result = 0
    for number in numbers:
        if is_positive(number):
            result += number
    return result


if __name__ == '__main__':
    print(calculate_sum_of_positives([int(input()) for i in range(3)]))
