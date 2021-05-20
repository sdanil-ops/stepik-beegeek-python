#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    The input to the program is the number n - the number
#    of dog years. Write a program that calculates
#    a dog's age in human years.
#    -----------------------------------------------------------
class Dog:
    def __init__(self, age: float):
        self.age = age
        self.dog_age = self.convert_to_dog_age(age)

    def convert_to_dog_age(self, age: float) -> float:
        if age < 3:
            return age * 10.5
        return (age * 4) + 13


if __name__ == '__main__':
    dog = Dog(float(input()))
    print(dog.dog_age)
