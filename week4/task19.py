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
        self.type = self.check_type()

    def is_equilateral(self):
        return self.x == self.y == self.z

    def is_isosceles(self):
        return self.x == self.y != self.z or self.x != self.y == self.z or self.x == self.z != self.y

    def check_type(self):
        if self.is_equilateral():
            return 'Равносторонний'
        if self.is_isosceles():
            return 'Равнобедренный'
        return 'Разносторонний'

    def __str__(self):
        return self.type


if __name__ == '__main__':
    # --------- testing ---------
    # tests = {
    #     'test 1': Triangle(145, 145, 139).__str__() == 'Равнобедренный',
    #     'test 2': Triangle(59, 59, 59).__str__() == 'Равносторонний',
    #     'test 3': Triangle(890, 199, 700).__str__() == 'Разносторонний',
    # }
    # flag = True
    # for test in tests:
    #     print(f'passed {test}' if tests[test] else f'{test} failed')
    #     if not tests[test]:
    #         flag = False
    # print('passed all tests' if flag else 'some tests failed')

    # --------- running ---------
    triangle = Triangle(int(input()), int(input()), int(input()))
    print(triangle)
