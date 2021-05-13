#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that takes a number as input and, depending
#    on the conditions, outputs the text "YES" or "NO".
#
#    Conditions:
#
#    if the number is odd, output "YES";
#    if the number is even in the range from 2 to 5 (inclusive), then output "NO";
#    if the number is even in the range from 6 to 20 (inclusive), then output "YES";
#    if the number is even and more than 20, then output "NO".
#    -----------------------------------------------------------
def check_number(number: int) -> bool:
    return is_odd(number) or (is_even(number) and 6 <= number <= 20)


def is_odd(number: int) -> bool:
    return number % 2 == 1


def is_even(number: int) -> bool:
    return number % 2 == 0


if __name__ == '__main__':
    print('YES' if check_number(int(input())) else 'NO')
