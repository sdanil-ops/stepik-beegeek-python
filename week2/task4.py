#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that outputs the specified triangle
#    consisting of asterisks (*)
#    -----------------------------------------------------------
class Triangle:
    def __init__(self, filler: str, side: int):
        self.filler = filler
        self.side = side

    def draw(self):
        for i in range(1, self.side + 1):
            print(self.filler * i)



if __name__ == '__main__':
    triangle = Triangle('*', 7)
    triangle.draw()
