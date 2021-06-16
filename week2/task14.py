#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Program that calculates the volume of a cube and its total
#    surface area, given entered value for the length of the edge
#    -----------------------------------------------------------
class Cube:
    def __init__(self, edge: int):
        self.edge = edge
        self.volume = self.calculate_cube_volume()
        self.area = self.calculate_cube_area()

    def calculate_cube_volume(self) -> int:
        """calculates volume of cube with known edge"""
        return self.edge ** 3

    def calculate_cube_area(self) -> int:
        """calculates area of cube with known edge edge"""
        return 6 * (self.edge ** 2)

    def __repr__(self):
        return f'Объем = {self.volume}\n'\
               f'Площадь полной поверхности = {self.area}'


# _________ test ____________
if __name__ == '__main__':
    print('testing', Cube.calculate_cube_volume, Cube.calculate_cube_area)
    cube = Cube(25)
    test_passed = cube.area == 3750 and cube.volume == 15625
    print('passed' if test_passed else 'failed')


#---------- run -------------
# if __name__ == '__main__':
#     cube = Cube(int(input()))
#     print(cube)
