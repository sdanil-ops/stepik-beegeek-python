#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    The weight of the amateur boxer is known (integer)
#    Write a program that determines which category a given
#    boxer will compete in.
#    -----------------------------------------------------------
class Boxer:
    def __init__(self, weight: int):
        self.weight = weight
        self.weight_group = self.get_weight_group(weight)

    def get_weight_group(self, weight: int) -> str:
        if self.is_lightweight(weight):
            return 'Легкий вес'
        if self.is_first_welterweight(weight):
            return 'Первый полусредний вес'
        if self.is_welterweight(weight):
            return 'Полусредний вес'

    def is_lightweight(self, weight: int) -> bool:
        return weight < 60

    def is_first_welterweight(self, weight: int) -> bool:
        return 60 <= weight < 64

    def is_welterweight(self, weight: int) -> bool:
        return 64 <= weight < 69


if __name__ == '__main__':
    boxer = Boxer(int(input()))
    print(boxer.weight_group)
