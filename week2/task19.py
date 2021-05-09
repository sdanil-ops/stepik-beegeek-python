#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    The program receives three integers as input: a1, d and n
#    Program should output  the nth term of the arithmetic progression.
#    -----------------------------------------------------------
def gen_n_term_of_arithmetic_progression(first: int, step: int, n: int) -> int:
    """returns n term of arithmetic progression starting from the first with a given step"""
    return first + step * (n - 1)


print(gen_n_term_of_arithmetic_progression(int(input()), int(input()), int(input())))
