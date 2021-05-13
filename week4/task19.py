#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that takes three positive numbers and
#    determines the shape of a triangle whose side lengths
#    are equal to the numbers you entered.
#    -----------------------------------------------------------
class Triangle:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
        self.type = self.Type(x=x, y=y, z=z)

    class Type:
        def __init__(self, x: int, y: int, z: int):
            self.type = self.check_type(x, y, z)

        def check_type(self, x: int, y: int, z: int):
            if self.is_equilateral(x, y, z):
                return 'Равносторонний'
            if self.is_isosceles(x, y, z):
                return 'Равнобедренный'
            return 'Разносторонний'

        def is_equilateral(self, x: int, y: int, z: int) -> bool:
            return x == y == z

        def is_isosceles(self, x: int, y: int, z: int) -> bool:
            return x == y != z or x != y == z or x == z != y


if __name__ == '__main__':
    triangle = Triangle(int(input()), int(input()), int(input()))
    print(triangle.type.type)
