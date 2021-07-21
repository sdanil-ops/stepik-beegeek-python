#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    program finds  number of meters for
#    a given number of centimeters.
#    -----------------------------------------------------------
class Distance:
    def __init__(self, meters: int = None, centimeters: int = None):
        if meters:
            self.meters = meters
            self.centimeters = self.convert_to_centimeters()
        elif centimeters:
            self.centimeters = centimeters
            self.meters = self.convert_to_meters()

    def convert_to_meters(self):
        return self.centimeters // 100

    def convert_to_centimeters(self):
        return self.meters * 100


# ------------ testing ------------
if __name__ == '__main__':
    test1_is_passed = Distance(centimeters=345).meters == 3
    print('passed test 1' if test1_is_passed else 'failed test 1')
    test2_is_passed = Distance(meters=3).centimeters == 300
    print('passed test 2' if test2_is_passed else 'failed test 2')


# ------------ running  ------------
# if __name__ == '__main__':
#     distance = Distance(centimeters=int(input()))
#     print(distance.meters)