#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Three different integers are given. Write a program that finds
#    the average number.
#    -----------------------------------------------------------
class ThreeNumbers:
    def __init__(self, number_list: list):
        self.average = self.AverageNumber(number_list)

    class AverageNumber:
        def __init__(self, number_list: list):
            self.value = self.get_average(number_list)

        def get_average(self, number_list: list) -> int:
            number_list.sort()
            return number_list[len(number_list) // 2]


if __name__ == '__main__':
    three_numbers = ThreeNumbers([int(input()) for i in range(3)])
    print(three_numbers.average.value)
