#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Mad Titan Thanos has collected all 6 Infinity Stones and
#    intends to destroy half the population of the Universe at
#    the snap of his fingers. Moreover, if the population of
#    the Universe is an odd number, then the titan will show mercy a
#    nd round up the number of survivors. Help the Avengers count
#    the number of survivors.
#    -----------------------------------------------------------
def count_number_of_survivors(population: int) -> int:
    """predicts count of survivors after Thanos attack"""
    return  population // 2 + population % 2


print(count_number_of_survivors(int(input())))