#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that reads two integers and a string
#    from the keyboard. If this line is a designation of
#    one of the four mathematical operations (+, -, *, /),
#    then output the result of applying this operation to
#    the numbers entered earlier, otherwise output
#    "Invalid operation". If the user wants to divide
#    by zero, output the text "You cannot divide by zero!"
#    -----------------------------------------------------------
def calculate(number: int, _number: int, operator: str)-> int or str:
    if operator == '+':
        return number + _number
    if operator == '-':
        return number - _number
    if operator == '*':
        return number * _number
    if operator == '/':
        return number / _number
    return 'Неверная операция'

try:
    print(calculate(int(input()), int(input()), input()))
except ZeroDivisionError:
    print('На ноль делить нельзя!')