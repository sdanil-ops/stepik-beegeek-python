#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that determines whether the rook can get
#    from the first square (x) to the second (y) in one move.
#    -----------------------------------------------------------
class Rook:

    def __init__(self, start_position):
        self.start_position = start_position


class RookMove(Rook):

    def is_possible_move(self, end_position) -> bool:
        return self.start_position[0] == end_position[0] or self.start_position[1] == end_position[1]


if __name__ == '__main__':
    # --------- testing ---------
    tests = {
        'test 1': RookMove((4, 4)).is_possible_move((5, 4)) is True,
        'test 2': RookMove((4, 4)).is_possible_move((5, 5)) is False,
        'test 3': RookMove((4, 4)).is_possible_move((4, 5)) is True
    }
    for test in tests:
        print(f'passed {test}' if tests[test] else f'failed {test}')

    # --------- running ---------
    # move = RookMove((int(input()), int(input()))).is_possible_move((int(input()), int(input())))
    # print('YES' if move else 'NO')
