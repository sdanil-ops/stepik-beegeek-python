#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    The program receives three lines as input, each on a separate line.
#    The program should output the entered lines in the same sequence,
#    each on a separate line.
#    -----------------------------------------------------------
def get_list_from_input(count: int = 3) -> list:
    """Returns list of inputted strings"""
    data = []
    for i in range(count + 1):
        data.append(input())
    return data


def print_list(data: list):
    """Prints unpacked list, each element on separate line"""
    print(*data, sep='\n')


print_list(get_list_from_input())
