""" Think Python Chapter 6, Exercise 6.4 (p.61)
jvdoorne, @Syntra, 18/10/2022
"""


def is_power(a, b):
    # if b == 0: raise ZeroDivisionError("Niet doen hé.")
    return a % b == 0 and is_power(a / b, b) if a > 1 else True


if __name__ == '__main__':
    print(is_power(8, 2))       # True
    print(is_power(27, 3))      # True
    print(is_power(27, 9))      # False
