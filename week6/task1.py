#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that reads the lengths of two legs
#    in a right-angled triangle and displays its area.
#    -----------------------------------------------------------
class RightTriangle:
    def __init__(self, leg: float, leg_: float):
        self.leg = leg
        self.leg_ = leg_
        self.area = self.calculate_triangle_area(leg, leg_)

    def calculate_triangle_area(self, leg: float, leg_: float) -> float:
        return 0.5 * leg * leg_


if __name__ == '__main__':
    triangle = RightTriangle(float(input()), float(input()))
    print(triangle.area)
