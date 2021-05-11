#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#     program compares the password and its confirmation.
#     If they match, the program displays: "Password accepted",
#     otherwise: "Password not accepted".
#    -----------------------------------------------------------
def is_same(password: str, confirmation: str) -> bool:
    """
    returns True if password and confirmation is same, otherwise returns False
    :param password:
    :param confirmation:
    :return:
    """
    return password == confirmation


def check_password(password: str, confirmation: str) -> str:
    """
    checks password
    :param password:
    :param confirmation:
    :return:
    """
    if is_same(password, confirmation):
        return 'Пароль принят'
    return 'Пароль не принят'


if __name__ == '__main__':
    print(check_password(input(), input()))
