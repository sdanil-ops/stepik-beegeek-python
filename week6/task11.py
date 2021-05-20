#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Five numbers are given. Write a program that calculates
#    the sum of their modules
#    -----------------------------------------------------------
def calculate_abs_sum(numbers: list) -> float:
    result = 0
    for i in range(len(numbers)):
        result += abs(numbers[i])
    return result


print(calculate_abs_sum([float(input()) for i in range(5)]))

