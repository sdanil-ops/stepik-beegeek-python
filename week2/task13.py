#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    program reads three integers and displays their sum.
#    Each number is written on a separate line.
#    -----------------------------------------------------------
def calculate_sum(count: int = 3):
    """Calculates sum of inputted numbers"""
    result = 0
    for i in range(count):
        result += int(input())
    return result


print(calculate_sum())
