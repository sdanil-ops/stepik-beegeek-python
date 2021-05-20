#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    program coverts celsius into farenheit and farenheit into celsius
#    -----------------------------------------------------------
class Temperature:
    def __init__(self, celsius: float = None, farenheit: float = None):
        if celsius is None:
            self.farenheit = farenheit
            self.celsius = self.convert_to_celsius(farenheit)
        if farenheit is None:
            self.celsius = celsius
            self.farenheit = self.convert_to_farenheit(celsius)

    def convert_to_celsius(self, farenheit: float) -> float:
        return (5 / 9) * (farenheit - 32)

    def convert_to_farenheit(self, celsius: float) -> float:
        return celsius * (9 / 5) + 32


if __name__ == '__main__':
    temperature = Temperature(farenheit=float(input()))
    print(temperature.celsius)
