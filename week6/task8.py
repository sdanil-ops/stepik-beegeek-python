#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that finds the smallest and largest of the five numbers.
#    -----------------------------------------------------------
def my_min(sequence: list)-> int:
    lower = sequence[0] # need to start with some value
    for i in sequence:
        if i < lower:
            lower = i
    return lower

def my_max(sequence: list)-> int:
    greater = sequence[0]
    for i in sequence:
        if i > greater:
            greater = i
    return greater


if __name__ == '__main__':
    numbers = [int(input()) for i in range(5)]
    print('Наименьшее число =', my_min(numbers))
    print('Наибольшее число =', my_max(numbers))
