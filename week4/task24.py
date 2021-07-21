#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Write a program that reads the names of the two primary
#    colors for mixing. If the user enters anything other than
#    red, blue, or yellow, the program should display an error
#    message. Otherwise, the program should print the name of
#    the secondary color that will be the result.
#    -----------------------------------------------------------
all_colors: dict = {'red': 'красный', 'yellow': 'желтый', 'blue': 'синий',
                    'purple': 'фиолетовый', 'green': 'зеленый', 'orange': 'оранжевый'}


class ColorMixer:
    def __init__(self, color: str, color_: str):
        self.color: str = self.mix_colors(color, color_)

    def mix_colors(self, color: str, color_: str) -> str:
        if self.is_purple(color, color_):
            return all_colors['purple']
        if self.is_green(color, color_):
            return all_colors['green']
        if self.is_orange(color, color_):
            return all_colors['orange']
        if self.is_same(color, color_):
            return color
        return 'ошибка цвета'

    def is_purple(self, color: str, color_: str) -> bool:
        return (color == all_colors['red'] and color_ == all_colors['blue']) or (
                color == all_colors['blue'] and color_ == all_colors['red'])

    def is_green(self, color: str, color_: str) -> bool:
        return (color == all_colors['yellow'] and color_ == all_colors['blue']) or (
                color == all_colors['blue'] and color_ == all_colors['yellow'])

    def is_orange(self, color: str, color_: str) -> bool:
        return (color == all_colors['red'] and color_ == all_colors['yellow']) or (
                color == all_colors['yellow'] and color_ == all_colors['red'])

    def is_same(self, color: str, color_: str) -> bool:
        return color == color_ == all_colors['red'] or color == color_ == all_colors['yellow'] or \
               color == color_ == all_colors['blue']


if __name__ == '__main__':
    color_mixer = ColorMixer(str(input()), str(input()))
    print(color_mixer.color)
