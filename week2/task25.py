#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    The compartment carriage has 9 compartments with four
#    passenger seats each. Write a program that determines
#    the number of the compartment in which the seat with
#    the given number is located
#    (the numbering of seats is through, starting with 1).
#    -----------------------------------------------------------
class Carriage:
    compartments_count: int = 9


class Compartment(Carriage):
    places_count: int = 4


class CompartmentPlace(Compartment):
    def __init__(self, number: int):
        self.number = number
        self.compartment_number = self.get_compartment_number()

    def get_compartment_number(self):
        return (self.number - 1) // self.places_count + 1


if __name__ == '__main__':
    place = CompartmentPlace(int(input()))
    print(place.compartment_number)
