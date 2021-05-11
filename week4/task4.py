#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that determines whether a user is allowed
#    access to an Internet resource or not.
#    -----------------------------------------------------------
def is_adult(age: int) -> bool:
    return age > 17


def check_access(age: int) -> str:
    if is_adult(age):
        return 'Доступ разрешен'
    return 'Доступ запрещен'


if __name__ == '__main__':
    print(check_access(int(input())))