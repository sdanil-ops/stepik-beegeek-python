#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that determines whether three given numbers
#    are consecutive members of an arithmetic progression.
#    -----------------------------------------------------------
def is_arithmetic_progression(number_list: list) -> bool:
    return number_list[1] - number_list[0] == number_list[2] - number_list[1]


def check_progression(number_list: list) -> str:
    if is_arithmetic_progression(number_list):
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    print(check_progression([int(input()) for i in range(3)]))

