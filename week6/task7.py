#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    A positive real number is given. Print its fractional part.
#    -----------------------------------------------------------
def get_fractional_part(number: float)-> float:
    return float(number - (int(number // 1)))

print(get_fractional_part(float(input())))