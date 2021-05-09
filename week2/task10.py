#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    a program reads a separator string and three lines,
#    and then prints the specified lines through the separator.
#    Uses code from task7. Just paste it
#    -----------------------------------------------------------
def get_list_from_input(count: int = 3) -> list:
    """Returns list of inputted strings"""
    data = []
    for i in range(count + 1):
        data.append(input())
    return data

def print_with_separator(data: list):
    """Prints string from inputted list, with first element as separator"""
    print(*data[1:], sep=data[0])


print_with_separator(get_list_from_input())
