#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Input is an integer, output is previous and next integer
#    -----------------------------------------------------------

def get_next_number(number: int) -> int:
    """returns next number"""
    return number + 1


def get_previous_number(number: int) -> int:
    """returns previous number"""
    return number - 1


def print_next_and_previous(number: int):
    """Prints next and previous number of given number"""
    print("Следующее за числом", number, "число:", get_next_number(number))
    print("Для числа", number, "предыдущее число:", get_previous_number(number))


print_next_and_previous(int(input()))