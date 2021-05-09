#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    program that reads a positive integer x
#    and displays a sequence of numbers x, x2, x3, x4, x5
#    -----------------------------------------------------------
def get_strange_sequence(number: int, lentht: int = 5, separator: str = '---') -> str:
    result = ''
    for i in range(1, lentht + 1):
        result += str(number * i)
        if i < lentht:
            result += separator
    return result


print(get_strange_sequence(int(input())))