""" Think Python Chapter 6, Exercise 6.5 (p.61)
jvdoorne, @Syntra, 18/10/2022
"""


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


if __name__ == '__main__':
    print(gcd(4, 16))   # 4
    print(gcd(16, 8))   # 8
