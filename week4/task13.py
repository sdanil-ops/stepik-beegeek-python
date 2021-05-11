#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Let's call a number beautiful if it is four-digit and
#    divisible by 7 or 17. Write a program that determines
#    whether the entered number is beautiful. The program
#    should print "YES" if the number is pretty, or "NO" otherwise.
#    -----------------------------------------------------------
def is_interesting_number(number: int) -> bool:
    return (1000 <= number <= 9999) and ((number % 7 == 0) or (number % 17 == 0))


def check_number_interestingness(number: int) -> str:
    if is_interesting_number(number):
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    print(check_number_interestingness(int(input())))
