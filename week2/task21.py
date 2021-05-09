#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Program receives three integers as input: a1, d and n
#    Program should output  the nth term of the geometric progression.
#    -----------------------------------------------------------
def get_n_term_of_geometric_progression(first: int, step: int, n: int) -> int:
    """returns n term of geometric progression starting from the first with a given step"""
    return first * (step ** (n - 1))


print(get_n_term_of_geometric_progression(int(input()), int(input()), int(input())))
