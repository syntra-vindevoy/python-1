import math


def estimate_pi():
    k = 0
    som = 0

    while True:
        y = math.factorial(4 * k) * (1103 + 26390 * k) / ((math.factorial(k)) ** 4 * 396 ** (4 * k))

        k += 1
        som += y

        if y < 1e-15:
            print(1/(2 * math.sqrt(2) * som / 9801))
            break


if __name__ == "__main__":
    estimate_pi()
    print(math.factorial(0))
