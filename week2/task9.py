#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#
#    program that displays the text "I *** like *** Python"
#    -----------------------------------------------------------
def print_love(name: str = 'Python', separator: str = '***'):
    """Prints 'I like' with specified name and separator"""
    print('I', 'like', name, sep=separator)


print_love()
