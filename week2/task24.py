#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Mad Titan Thanos has collected all 6 Infinity Stones and
#    intends to destroy half the population of the Universe at
#    the snap of his fingers. Moreover, if the population of
#    the Universe is an odd number, then the titan will show mercy a
#    nd round up the number of survivors. Help the Avengers count
#    the number of survivors.
#    -----------------------------------------------------------
from task1 import TestUnit


class Population:
    def __init__(self, population: int):
        self.population = population
        self.survivors = self.count_survivors()

    def count_survivors(self):
        return self.population // 2 + self.population % 2

    def __repr__(self):
        return str(self.survivors)


# ------------- testing -------------
# if __name__ == '__main__':
#     test = TestUnit(Population, 99, '50')
#     print('passed' if test.is_passed else 'failed')


# ------------- running -------------
if __name__ == '__main__':
    univerce_population = Population(int(input()))
    print(univerce_population)