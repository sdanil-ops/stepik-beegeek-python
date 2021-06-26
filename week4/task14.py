#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that takes three positive numbers
#    and determines if there is a non-degenerate triangle
#    with such sides.
#    -----------------------------------------------------------
class Triangle:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
        self.is_existence = self.is_existence_triangle()
        self.is_non_degraded = 'YES' if self.is_existence else 'NO'

    def is_existence_triangle(self):
        return (self.x < self.y + self.z) and (self.y < self.x + self.z) and (self.z < self.x + self.y)


if __name__ == '__main__':
    # ------------- testing -------------
    # tests = {
    #     'test 1': Triangle(5, 2, 3).is_non_degraded == 'NO',
    #     'test 2': Triangle(3, 4, 6).is_non_degraded == 'YES',
    #     'test 3': Triangle(8, 2, 4).is_non_degraded == 'NO'
    # }
    # for test in tests:
    #     print(f'passed {test}' if tests[test] else f'failed {test}')

    # ------------- running -------------
    triangle = Triangle(int(input()), int(input()), int(input()))
    print(triangle.is_non_degraded)
