#    -----------------------------------------------------------
#    Copyright (c) 2021. Danil Smirnov
#    n schoolchildren divide k mandarins equally,
#    the non-dividing remainder remains in the basket.
#    How many whole tangerines will each student get?
#    How many whole tangerines are left in the basket?
#    -----------------------------------------------------------
from typing import Tuple


def distribute_tangerines(recipients: int, tangerines: int) -> Tuple[int, int]:
    """
    returns number of tangerines that each recipient will
    get and the number of tangerines that will remain in the basket
    """
    return tangerines // recipients, tangerines % recipients


print(*distribute_tangerines(int(input()), int(input())), sep='\n')
