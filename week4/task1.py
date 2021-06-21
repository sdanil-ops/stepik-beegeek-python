#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#     program compares the password and its confirmation.
#     If they match, the program displays: "Password accepted",
#     otherwise: "Password not accepted".
#    -----------------------------------------------------------
class Password:
    password: str or int


class PasswordConfirmation(Password):
    def __init__(self, password: str or int, confirmation: str or int):
        self.password = password
        self.confirmation = confirmation
        self.is_valid = self.is_valid_password()

    def is_valid_password(self):
        return self.password == self.confirmation

    def __repr__(self):
        if self.is_valid:
            return 'Пароль принят'
        return 'Пароль не принят'


# ------------ testing ------------
# if __name__ == '__main__':
#     test_is_passed = PasswordConfirmation(123, 123).__repr__() == 'Пароль принят'
#     print('test 1 is passed' if test_is_passed else 'test 1 is failed')
#     test_is_passed = PasswordConfirmation(123, 321).__repr__() == 'Пароль не принят'
#     print('test 2 is passed' if test_is_passed else 'test 2 is failed')
# ------------ running ------------
if __name__ == '__main__':
    password = PasswordConfirmation(input(), input())
    print(password)
