#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that outputs the specified triangle
#    consisting of asterisks (*)
#    -----------------------------------------------------------

def print_triangle(filler: str = '*', side: int = 7):
    """Prints triangle with specified filler and side"""
    for i in range(side + 1):
        print(filler * i)


print_triangle()
