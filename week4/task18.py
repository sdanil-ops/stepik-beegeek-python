#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Zoom challenged Flash and offered him a fair fight in the
#    form of a race. If Zoom is faster than Flash, you need
#    to output "NO", if Flash is faster than Zoom, you need
#    to output "YES", if their speeds are equal, you need to
#    output "Don't know".
#    -----------------------------------------------------------
class SpeedstersRace:
    zoom_speed: int
    flash_speed: int
    winner: str

    class SpeedstersRaceWinner:

        def __init__(self, zoom_speed: int, flash_speed):
            SpeedstersRace.zoom_speed = zoom_speed
            SpeedstersRace.flash_speed = flash_speed
            SpeedstersRace.winner = self.get_winner()

        def get_winner(self):
            if SpeedstersRace.zoom_speed == SpeedstersRace.flash_speed:
                return "Don't know"
            if SpeedstersRace.zoom_speed > SpeedstersRace.flash_speed:
                return "NO"
            return "YES"

        def __str__(self):
            return SpeedstersRace.winner


if __name__ == '__main__':
    # --------- testing ---------
    # tests = {
    #     'test 1': SpeedstersRace.SpeedstersRaceWinner(2204, 1505).__str__() == "NO",
    #     'test 2': SpeedstersRace.SpeedstersRaceWinner(2344, 4324).__str__() == "YES",
    #     'test 3': SpeedstersRace.SpeedstersRaceWinner(2500, 2500).__str__() == "Don't know"
    # }
    # flag = True
    # for test in tests:
    #     print(f'passed {test}' if tests[test] else f"{test} failed")
    #     if not tests[test]:
    #         flag = False
    # print('all tests was passed' if flag else 'not all tests was passed')
    #
    # --------- running ---------
    winner = SpeedstersRace.SpeedstersRaceWinner(int(input()), int(input()))
    print(winner)

