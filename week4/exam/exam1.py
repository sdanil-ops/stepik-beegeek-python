#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that determines whether a year with a given
#    number ends with two zeros. If the year ends, then output "YES",
#    otherwise output "NO".Write a program that determines whether
#    a year with a given number ends with two zeros.
#    If the year ends, then output "YES", otherwise output "NO".
#    -----------------------------------------------------------
def is_century_beginning(year: int) -> bool:
    return year % 10 == year % 100 // 10 == 0


def check_year(year: int) -> str:
    if is_century_beginning(year):
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    print(check_year(int(input())))