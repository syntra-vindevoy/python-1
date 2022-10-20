import math


def recursive(n):
    x = 1
    while n > 0:
        x = x * n
        n -= 1
    return x


def term(n):
    return (2 * (2 ** 0.5) / 9801) * (recursive(4*n) * (1103 + 26390 * n)) / ((recursive(n) ** 4) * 396 ** (4*n))


k = 0

estimated_pi = 0

while term(n=k) > 0.1 ** 15:
    estimated_pi += term(n=k)
    k += 1


print(k, 1/estimated_pi, math.pi)
