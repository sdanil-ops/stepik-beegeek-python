#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that orders three numbers from highest to lowest
#    -----------------------------------------------------------
def insertion_sort(unsorted_list: list):
    """ sorting list A by insertion method """
    length = len(unsorted_list)
    for top in range(1, length):
        pos = top                         # k - position
        while pos > 0 and unsorted_list[pos - 1] > unsorted_list[pos]:  # prevents out of bounce
            unsorted_list[pos], unsorted_list[pos - 1] = unsorted_list[pos - 1], unsorted_list[pos]
            pos -= 1


if __name__ == '__main__':
    numbers = [int(input()) for i in range(3)]
    insertion_sort(numbers)
    print(*numbers[::-1], sep='\n')
