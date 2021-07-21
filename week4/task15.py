#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that determines whether a given year
#    is a leap year. If the year is a leap year,
#    then output "YES", otherwise output "NO".
#    -----------------------------------------------------------
class Year:
    def __init__(self, year: int):
        self.year = year
        self.is_leap = self.is_leap()

    def is_leap(self) -> bool:
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    def __repr__(self):
        return 'YES' if self.is_leap else 'NO'


if __name__ == '__main__':
    # ---------- testing ----------

    tests = {
        'test 1': Year(2020).is_leap is True,
        'test 2': Year(2012).is_leap is True,
        'test 3': Year(2009).is_leap is not True
    }
    for test in tests:
        print(f'passed {test}' if tests[test] else f'failed {test}')

    # ---------- running ----------

    # year = Year(int(input()))
    # print(year)
