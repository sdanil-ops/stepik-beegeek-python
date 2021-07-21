#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Reproduction n. If n = 1 > 1 + 11 + 111 = 123
#    -----------------------------------------------------------
def reproduct(number: int) -> int:
    return (number * 10) + number + ((((number * 10) + number) * 10) + number) + number


if __name__ == '__main__':
    print(reproduct(int(input())))
