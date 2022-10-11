""" Find a way to predict the length of an integer.
jvdoorne, @Syntra, 11/10/2022
"""

import math
from fibonacci import fibo_no_recurse


def len_int(n):
    return int(math.log10(n)) + 1


if __name__ == '__main__':
    assert len_int(123456789) == 9
    assert len_int(fibo_no_recurse(500)) == 105
