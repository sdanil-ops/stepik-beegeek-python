#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    program finds  number of meters for
#    a given number of centimeters.
#    -----------------------------------------------------------
def convert_to_meters(sm: int) -> int:
    """converts centimeters to meters"""
    return sm // 100


print(convert_to_meters(int(input())))
