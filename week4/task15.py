#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that determines whether a given year
#    is a leap year. If the year is a leap year,
#    then output "YES", otherwise output "NO".
#    -----------------------------------------------------------
def is_leap(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def check_year(year: int) -> str:
    if is_leap(year):
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    print(check_year(int(input())))
