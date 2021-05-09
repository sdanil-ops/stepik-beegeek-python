#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    The program receives one line as input - name.
#    Output must be "Привет, $name". Uses similar with task 1 code.
#    to complete task remove
#    -----------------------------------------------------------

def say_hello(name: str = None):
    """Prints greeting to specified name"""
    if name is None:
        name = input()
    print(f'Привет, {name}')


say_hello()
