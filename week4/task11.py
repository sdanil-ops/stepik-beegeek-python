#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that takes an integer xxx and determines
#    whether the given number belongs to the specified ranges.
#    -----------------------------------------------------------
from task10 import is_in_interval


def check_affiliation(number: int) -> str:
    if is_in_interval(number, (-3, 7)):
        return 'Не принадлежит'
    return 'Принадлежит'


if __name__ == '__main__':
    print(check_affiliation(int(input())))
