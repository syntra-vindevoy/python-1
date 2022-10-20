""" Think Python Chapter 7, Exercise 7.3 (p.70)
jvdoorne, @Syntra, 20/10/2022
"""

from math import factorial, pi, sqrt


def estimate_pi():
    k, summation = 0, 0
    while True:
        # Compute next term in series
        t = (factorial(4 * k) * (1103 + 26390 * k)) / \
            ((factorial(k) ** 4) * (396 ** (4 * k)))
        summation += t
        if t < 1e-15:
            # Calculate estimated value of π
            return 9801 / (2 * sqrt(2) * summation)
        k += 1


if __name__ == '__main__':
    e = estimate_pi()
    print(f"π = {e} (diff={abs(pi - e)})")
