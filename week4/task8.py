#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that, according to the entered age of the user,
#    tells which age group he belongs to
#    -----------------------------------------------------------
class User:
    def __init__(self, age: int):
        self.age = age
        self.age_group = self.get_age_group()

    def is_old(self) -> bool:
        return self.age >= 60

    def is_mature(self) -> bool:
        return 59 >= self.age >= 25

    def is_young(self) -> bool:
        return 24 >= self.age >= 14

    def is_child(self) -> bool:
        return 13 >= self.age

    def get_age_group(self):
        if self.is_old():
            return 'старость'
        if self.is_mature():
            return 'зрелость'
        if self.is_young():
            return 'молодость'
        if self.is_child():
            return 'детство'


if __name__ == '__main__':
    # ---------- testing ----------
    # tests = {
    #     'test 1': User(age=4).age_group == 'детство',
    #     'test 2': User(age=91).age_group == 'старость',
    #     'test 3': User(age=40).age_group == 'зрелость'
    # }
    # for test in tests:
    #     print(f'passed {test}' if tests[test] else f'failed {test}')

    # ---------- running ----------
    user = User(age=int(input()))
    print(user.age_group)
