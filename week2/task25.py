#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    The compartment carriage has 9 compartments with four
#    passenger seats each. Write a program that determines
#    the number of the compartment in which the seat with
#    the given number is located
#    (the numbering of seats is through, starting with 1).
#    -----------------------------------------------------------
def get_compartment_number(place_number: int, places: int = 4, starts_from: int = 1) -> int:
    """returns compartment number by given place number"""
    return (place_number - starts_from) // places + starts_from


print(get_compartment_number(int(input())))

