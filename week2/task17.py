#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    program that calculates the cost of three computers,
#    consisting of a monitor, system unit, keyboard and mouse.
#
#    -----------------------------------------------------------
def calculate_price_of_set(components: int = 4, count: int = 3) -> int:
    """calculates full price of given set of components"""
    result = 0
    for i in range(components):
        result += int(input())
    return result * count


print(calculate_price_of_set())

