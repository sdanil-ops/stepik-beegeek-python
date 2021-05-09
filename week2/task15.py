#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    f(a,b) =3(a+b)**3 + 275b**2 − 127a−41
#    program for calculating the value of a function
#    -----------------------------------------------------------
def calculate_strange_function(a: int, b: int) -> int:
    """Calculates value of a function f(a,b) =3(a+b)**3 + 275b**2 − 127a−41"""
    return (3 * ((a + b) * (a + b) * (a + b))) + (275 * (b * b)) - (127 * a) - 41


print(calculate_strange_function(int(input()), int(input())))
