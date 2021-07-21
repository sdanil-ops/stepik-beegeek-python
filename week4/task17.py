#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that determines whether the king can get
#    from the first square (x) to the second (y) in one move.
#    -----------------------------------------------------------
from typing import Tuple


class Position:

    def __init__(self, coordinates: Tuple[int, int]):
        self.x = coordinates[0]
        self.y = coordinates[1]


class KingMove:

    def __init__(self, start_position: Position, end_position: Position):
        self.start_position = start_position
        self.end_position = end_position

    def is_possible_king_move(self):
        return -1 <= self.start_position.x - self.end_position.x <= 1 and \
               -1 <= self.start_position.y - self.end_position.y <= 1


if __name__ == '__main__':
    # --------- testing ---------
    # tests = {
    #     'test 1': KingMove(Position((4, 4)), Position((5, 5))).is_possible_king_move() is True,
    #     'test 2': KingMove(Position((4, 4)), Position((5, 4))).is_possible_king_move() is True,
    #     'test 3': KingMove(Position((4, 4)), Position((2, 4))).is_possible_king_move() is False,
    # }
    # flag = True
    # for test in tests:
    #     print(f'passed {test}' if tests[test] else f'failed {test}')
    #     if not tests[test]:
    #         flag = False
    # print('all tests was passed' if flag else 'not all tests was passed')

    # --------- running ---------
    move = KingMove(Position((int(input()), int(input()))), Position((int(input()), int(input()))))
    print('YES' if move.is_possible_king_move() else 'NO')

