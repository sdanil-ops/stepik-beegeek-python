#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that determines the smallest of two numbers
#    -----------------------------------------------------------

def is_lesser(a: int, b: int) -> bool:
    return a < b


def get_lesser_of_two(a: int, b: int) -> int:
    if is_lesser(a, b):
        return a
    return b


if __name__ == '__main__':
    print(get_lesser_of_two(int(input()), int(input())))
