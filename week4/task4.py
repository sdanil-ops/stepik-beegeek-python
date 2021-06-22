#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that determines whether a user is allowed
#    access to an Internet resource or not.
#    -----------------------------------------------------------
class User:
    def __init__(self, age: int):
        self.age = age
        self.is_adult = self.is_adult()
        self.access = self.check_access()

    def is_adult(self):
        return self.age > 17

    def check_access(self):
        if self.is_adult:
            return 'Доступ разрешен'
        return 'Доступ запрещен'


# ------------- testing -------------
# if __name__ == '__main__':
    # test_is_passed = User(age=16).access == 'Доступ запрещен'
    # print('test 1 is passed' if test_is_passed else 'failed test 1')
    # test_is_passed = User(age=18).access == 'Доступ разрешен'
    # print('test 2 is passed' if test_is_passed else 'failed test 2')
    # test_is_passed = User(age=19).access == 'Доступ разрешен'
    # print('test 3 is passed' if test_is_passed else 'failed test 3')

# ------------- running -------------
if __name__ == '__main__':
    user = User(age=int(input()))
    print(user.access)
