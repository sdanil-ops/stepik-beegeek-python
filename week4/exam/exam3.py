#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    The football team recruits girls from 10 to 15 years old inclusive.
#    Write a program that asks for the age and gender of an applicant
#    using the gender designation m (for male) and f (for female)
#    to determine if the applicant is eligible to join the team or not.
#    If the applicant fits, then output "YES", otherwise output "NO".
#    -----------------------------------------------------------
class Applicant:
    def __init__(self, name: str = None, age: int = None, gender: str = None):
        self.name = name
        self.age = age
        self.gender = gender
        self.can_join = self.check_membership(age, gender)

    def check_membership(self, age: int, gender: str) -> bool:
        return self.check_age(age) and self.check_gender(gender)

    def check_age(self, age: int) -> bool:
        return 10 <= age <= 15

    def check_gender(self, gender: str) -> bool:
        return gender == 'f'


if __name__ == '__main__':
    applicant = Applicant(age=int(input()), gender=input())
    print('YES' if applicant.can_join else 'NO')
