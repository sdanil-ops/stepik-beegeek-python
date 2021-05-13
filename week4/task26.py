#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    There are two segments on the number line. Write a program
#    that finds their intersection.
#    program should display the boundaries of the segment
#    that is the intersection, either a common point, or the text "empty set".
#    -----------------------------------------------------------
class Section:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


class Crossing:
    def __init__(self, section: Section, section_: Section):
        self.intersection = self.get_crossing(section, section_)
        self.empty = self.is_empty(section, section_)

    def get_crossing(self, section: Section, section_: Section):
        if self.is_empty(section, section_):
            return 'пустое множество'
        if self.is_point(section, section_):
            return min(section.end, section_.end)
        result = max(section.start, section_.start), min(section.end, section_.end)
        return result

    def is_empty(self, section: Section, section_: Section) -> bool:
        return min(section.end, section_.end) < max(section.start, section_.start)

    def is_point(self, section: Section, section_: Section) -> bool:
        return min(section.end, section_.end) == max(section.start, section_.start)

if __name__ == '__main__':
    section_1 = Section(int(input()), int(input()))
    section_2 = Section(int(input()), int(input()))
    crossing = Crossing(section_1, section_2)
    if type(crossing.intersection) == tuple:
        print(*crossing.intersection)
    else:
        print(crossing.intersection)
