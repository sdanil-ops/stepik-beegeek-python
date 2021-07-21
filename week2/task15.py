#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    f(a,b) =3(a+b)**3 + 275b**2 − 127a−41
#    program for calculating the value of a function
#    -----------------------------------------------------------
class StrangeFunction:
    def __init__(self, value_a: int, value_b: int):
        self.value_a = value_a
        self.value_b = value_b
        self.value = self.calculate()

    def calculate(self):
        return (3 * ((self.value_a + self.value_b) * (self.value_a + self.value_b) * (self.value_a + self.value_b))) + \
               (275 * (self.value_b * self.value_b)) - (127 * self.value_a) - 41


# --------------- - - test - - ----------------
# if __name__ == '__main__':
#     print('testing: ', StrangeFunction.calculate)
#     func = StrangeFunction(1, 1)
#     test_is_passed = func.value == 131
#     print('passed' if test_is_passed else 'failed')


# --------------- - - run!  - - ------------------
if __name__ == '__main__':
    my_function = StrangeFunction(int(input()), int(input()))
    print(my_function.value)
