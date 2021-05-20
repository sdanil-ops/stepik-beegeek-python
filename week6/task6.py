#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    A positive real number is given.
#    Print its first digit after the decimal point
#    -----------------------------------------------------------
def get_first_decimal_place(number: float)-> int:
    return int((number * 10) % 10)

print(get_first_decimal_place(float(input())))