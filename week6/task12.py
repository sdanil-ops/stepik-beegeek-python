#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that calculates taxicab distance
#    between two given coordinates.
#    -----------------------------------------------------------
def calculate_taxicab_distance(p: int, p_: int, q: int, q_: int)-> int:
    return abs(p - q) + abs(p_ - q_)

print(calculate_taxicab_distance(int(input()), int(input()), int(input()), int(input())))


