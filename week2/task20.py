#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    program that reads a positive integer x
#    and displays a sequence of numbers x, x2, x3, x4, x5
#    -----------------------------------------------------------
from task10 import StringsWithSeparator
from task1 import TestUnit

# --------- testing ----------
# if __name__ == '__main__':
#     test = TestUnit(StringsWithSeparator, ['7', '14', '21', '28', '35'], '7***14***21***28***35')
#     print('passed' if test.is_passed else 'failed')


# -------- running ----------
if __name__ == '__main__':
    value = int(input())
    sequence = [value * i for i in range(1, 6)]
    for i in range(len(sequence)):
        sequence[i] = str(sequence[i])
    result = StringsWithSeparator(sequence, separator='---')
    print(result)
