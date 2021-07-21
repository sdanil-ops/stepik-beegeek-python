#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    The ordinal number of the month is given (1,2, ..., 12).
#    Write a program that displays the number of days
#    in this month. Accept that the year is not a leap year.
#    -----------------------------------------------------------
class Month:
    def __init__(self, month_number: int):
        self.length = self.get_length(month_number)

    def get_length(self, month_number: int):
        return 30 + (month_number - 6) % 2 + (2 * ((month_number + 1) % 2) - 1) * \
               (month_number // 8) - 2 * (((month_number - 3) % 12) // 11)


if __name__ == '__main__':
    month = Month(int(input()))
    print(month.length)
