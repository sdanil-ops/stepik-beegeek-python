#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Zoom challenged Flash and offered him a fair fight in the
#    form of a race. If Zoom is faster than Flash, you need
#    to output "NO", if Flash is faster than Zoom, you need
#    to output "YES", if their speeds are equal, you need to
#    output "Don't know".
#    -----------------------------------------------------------
class SpeedstersRace:
    def __init__(self, zoom_speed: int, flash_speed: int):
        self.zoom_speed = zoom_speed
        self.flash_speed = flash_speed

    def get_winner(self):
        if self.zoom_speed == self.flash_speed:
            return "Don't know"
        if self.zoom_speed > self.flash_speed:
            return "NO"
        return "YES"


if __name__ == '__main__':
    race = SpeedstersRace(zoom_speed=int(input()), flash_speed=int(input()))
    print(race.get_winner())
