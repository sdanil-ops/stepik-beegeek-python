#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that reads in an integer and outputs
#    the corresponding Roman numeral. If the number is outside
#    the range of 1-10, then the program should display
#     text "error".
#    -----------------------------------------------------------
def get_roman(arabic: int) -> str:
    thousands = ['', 'M', 'MM', 'MMM', 'MMMM']
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

    th = thousands[arabic // 1000]
    hn = hundreds[arabic // 100 % 10]
    ts = tens[arabic // 10 % 10]
    on = ones[arabic % 10]

    return th + hn + ts + on


if __name__ == '__main__':
    arabic_number = int(input())
    if arabic_number not in set(list(range(1, 11))):
        print('ошибка')
    else:
        print(get_roman(arabic_number))

