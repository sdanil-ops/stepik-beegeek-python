#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that, according to the entered age of the user,
#    tells which age group he belongs to
#    -----------------------------------------------------------
def is_old(age: int) -> bool:
    return age >= 60


def is_mature(age: int) -> bool:
    return 59 >= age >= 25


def is_young(age: int) -> bool:
    return 24 >= age >= 14


def is_child(age: int) -> bool:
    return 13 >= age


def get_age_group(age: int) -> str:
    if is_old(age):
        return 'старость'
    if is_mature(age):
        return 'зрелость'
    if is_young(age):
        return 'молодость'
    if is_child(age):
        return 'детство'


if __name__ == '__main__':
    print(get_age_group(int(input())))
