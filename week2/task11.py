#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    a program that greets the user by outputting the word
#    "Привет" (without quotes), followed by a comma and space,
#    followed by the name and exclamation point entered.
#    -----------------------------------------------------------
def say_hello(name: str = None):
    """Prints hello to a specified name"""
    if name is None:
        name = input()
    print(f'Привет, {name}!')


say_hello()
