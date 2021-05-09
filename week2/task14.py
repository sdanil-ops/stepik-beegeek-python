#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Program that calculates the volume of a cube and its total
#    surface area, given entered value for the length of the edge
#    -----------------------------------------------------------
def calculate_cube_volume(edge: int) -> int:
    """calculates volume of cube with known edge"""
    return edge ** 3


def calculate_cube_area(edge: int) -> int:
    """calculates area of cube with known edge edge"""
    return 6 * (edge ** 2)


def print_cube_area_and_volume(edge: int):
    """Calculates and prints area and volume of cube with known edge """
    print("Объем =", calculate_cube_volume(edge))
    print("Площадь полной поверхности =", calculate_cube_area(edge))


print_cube_area_and_volume(int(input()))
