import math


def recursive(n):
    x = 1
    while n > 0:
        x = x * n
        n -= 1
    return x


k = 0
term = (2 * (2 ** 0.5) / 9801) * (recursive(4*k) * (1103 + 26390 * k)) / ((recursive(k) ** 4) * 396 ** (4*k))
estimated_pi = 0

while term > 0.1 ** 15:
    term = (2 * (2 ** 0.5) / 9801) * (recursive(4*k) * (1103 + 26390 * k)) / ((recursive(k) ** 4) * 396 ** (4*k))
    k += 1
    estimated_pi += term


print(k, 1/estimated_pi, math.pi)
