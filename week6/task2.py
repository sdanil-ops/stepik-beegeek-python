#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    Two old ladies are walking towards each other at constant
#    speeds V1 and V2 km / h. Determine how long the old ladies
#    will meet if the distance between them is S km.
#    -----------------------------------------------------------
class OldLady: # speed V
    def __init__(self, speed: float):
        self.speed = speed


class Appointment: # distance S
    def __init__(self, distance: float, object1: OldLady, object2: OldLady):
        self.distance = distance
        self.appointment_time = self.get_appointment_time(object1, object2)
        print(f'distance {distance}')


    def get_appointment_time(self, object1: OldLady, object2: OldLady):
        return self.distance / (object1.speed + object2.speed)


if __name__ == '__main__':
    meeting_time = Appointment(float(input()), OldLady(float(input())), OldLady(float(input()))).appointment_time
    print(meeting_time)
