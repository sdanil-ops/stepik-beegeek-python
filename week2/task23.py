#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    n schoolchildren divide k mandarins equally,
#    the non-dividing remainder remains in the basket.
#    How many whole tangerines will each student get?
#    How many whole tangerines are left in the basket?
#    -----------------------------------------------------------
class Distribute:
    def __init__(self, recipients_count: int, product_count: int):
        self.recipients_count = recipients_count
        self.product_count = product_count

    def distribute(self):
        return self.product_count // self.recipients_count, self.product_count % self.recipients_count


if __name__ == '__main__':
    tangerines = Distribute(int(input()), int(input()))
    print(*tangerines.distribute(), sep='\n')
