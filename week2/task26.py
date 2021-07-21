#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    program for converting the value of the time interval
#    specified in minutes into the value expressed
#    in hours and minutes.
#    -----------------------------------------------------------
from task1 import TestUnit


class TimeInterval:
    def __init__(self, minutes: int):
        self.minutes = minutes
        self.complete_hours = self.get_complete_hours()
        self.rest_minutes = self.get_rest_minutes()

    def get_complete_hours(self):
        """returns the number of complete hours"""
        return self.minutes // 60

    def get_rest_minutes(self):
        """returns the number of minutes remaining"""
        return self.minutes % 60

    def __repr__(self):
        return f'{self.minutes} мин - это {self.complete_hours} час {self.rest_minutes} минут.'


# ------------- testing -------------
if __name__ == '__main__':
    test = TestUnit(TimeInterval, 150, '150 мин - это 2 час 30 минут.')
    print('passed' if test.is_passed else 'failed')

# ------------- running -------------
# if __name__ == '__main__':
#     time_interval = TimeInterval(int(input()))
#     print(time_interval)
