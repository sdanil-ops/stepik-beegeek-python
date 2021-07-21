# -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov Write a program that
#    reads the pocket number and indicates whether the pocket is green,
#    red, or black. The program should display an
#    error message if the user enters a number that is outside
#    the range from 0 to 36.
#    -----------------------------------------------------------
class Roulette:
    def __init__(self, sector: int):
        self.sector_color = self.get_sector_color(sector)

    def get_sector_color(self, sector: int) -> str:
        if sector == 0:
            return 'зеленый'
        else:
            if self.is_valid(sector):
                if self.is_black(sector):
                    return 'черный'
                return 'красный'
            return 'ошибка ввода'

    def is_black(self, sector: int):
        return (1 <= sector <= 10 and sector % 2 == 0) or (11 <= sector <= 18 and sector % 2 != 0) or \
               (19 <= sector <= 28 and sector % 2 == 0) or (29 <= sector <= 36 and sector % 2 != 0)

    def is_valid(self, sector: int):
        return 0 <= sector <= 36


if __name__ == '__main__':
    roll = Roulette(int(input()))
    print(roll.sector_color)
