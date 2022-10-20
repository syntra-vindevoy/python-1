""" Think Python Chapter 7, Exercise 7.1 (p.69)
jvdoorne, @Syntra, 20/10/2022
"""

import math


def mysqrt(a):
    x = a / 2
    while True:
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    return x


def test_square_root():
    # Table header
    print(f"{'a':<18} {'mysqrt(a)':<18} {'diff':<18}")
    print(f"{'-':<18} {'---------':<18} {'----':<18}")
    # Table body
    for i in range(1, 10):
        a, b = mysqrt(i), math.sqrt(i)
        print(f"{a:<18} {b:<18} {abs(a-b):<18}")


if __name__ == '__main__':
    test_square_root()
