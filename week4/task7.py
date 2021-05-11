#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that determines the smallest of four numbers
#    -----------------------------------------------------------
def get_minimal_element(number_list: list) -> int:
    if len(number_list) == 2:
        if number_list[0] < number_list[1]:
            return number_list[0]
        return number_list[1]
    result = get_minimal_element(number_list[1:])
    if number_list[0] < result:
        return number_list[0]
    return result


if __name__ == '__main__':
    print(get_minimal_element([int(input()) for i in range(4)]))
