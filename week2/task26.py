#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    program for converting the value of the time interval
#    specified in minutes into the value expressed
#    in hours and minutes.
#    -----------------------------------------------------------
def get_complete_hours(minutes: int) -> int:
    """returns the number of complete hours"""
    return minutes // 60


def get_rest_minutes(minutes: int) -> int:
    """returns the number of minutes remaining"""
    return minutes % 60


def convert_to_hours_and_minutes(minutes: int) -> str:
    """returns minutes expressed in hours and minutes."""
    return f'{minutes} мин - это {get_complete_hours(minutes)} час {get_rest_minutes(minutes)} минут.'


print(convert_to_hours_and_minutes(int(input())))
