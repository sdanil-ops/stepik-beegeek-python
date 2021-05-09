#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    The input to the program is four positive integers
#    a, b, c and d, each on a separate line in the specified order.
#    -----------------------------------------------------------
def calculate_exponentiation_amount(a: int, b: int, c: int, d: int) -> int:
    return (a ** b) + (c ** d)


if __name__ == '__main__':
    print(calculate_exponentiation_amount(int(input()), int(input()), int(input()), int(input())))
