#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that takes three positive numbers
#    and determines if there is a non-degenerate triangle
#    with such sides.
#    -----------------------------------------------------------
def is_existence_triangle(x: int, y: int, z: int) -> bool:
    return (x < y + z) and (y < x + z) and (z < x + y)


def check_triangle(x: int, y: int, z: int) -> str:
    if is_existence_triangle(x, y, z):
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    print(check_triangle(int(input()), int(input()), int(input())))
