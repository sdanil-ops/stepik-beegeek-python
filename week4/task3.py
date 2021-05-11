#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that checks that for a given four-digit number,
#    the following relationship holds: the sum of the first and
#    last digits is equal to the difference between the second
#    and third digits.
#    -----------------------------------------------------------
def calculate_sum_of_last_and_first_digits(number: int) -> int:
    """returns sum of first and last digits of inputted number"""
    return (number % 10) + ((number % 10 ** 4) // 10 ** 3)


def calculate_difference_between_last_and_first_digits(number: int) -> int:
    """returns difference between first and last digits of inputted number"""
    return ((number % 10 ** 3) // 10 ** 2) - (number % 10 ** 2) // 10 ** 1


def check_ratio(number: int) -> str:
    """returns YES if ratio is fulfilled, else NO"""
    if calculate_sum_of_last_and_first_digits(number) == calculate_difference_between_last_and_first_digits(number):
        return 'ДА'
    return 'НЕТ'


if __name__ == '__main__':
    print(check_ratio(int(input())))
