#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that prints a rectangle with asterisks (*) around its perimeter.
#    Note. The height and width of the rectangle are 4 and 17 stars, respectively.
#    -----------------------------------------------------------
def print_rectangle(filler: str = '*', height: int = 4, width: int = 17):
    print(filler * width)
    print(filler, ' ' *(width - height), filler)
    print(filler, ' ' *(width - height), filler)
    print(filler * width)



if __name__ == '__main__':
    print_rectangle()
