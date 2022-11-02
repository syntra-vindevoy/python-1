import math


def mysqrt(a, x):
    epsilon = 0.00000001
    while True:
        # print(x)
        y = (x + a / x) / 2

        if abs(y - x) < epsilon:
            break

        x = y
    return y


def test_square_root():
    print("a" + 3 * " " + "mysqrt(a)" + 5 * " " + "math.sqrt(a)" + 2 * " " + "diff")
    print("-" + 3 * " " + "---------" + 5 * " " + "------------" + 2 * " " + "----")
    for i in range(1, 10, 1):
        print(round(float(i), 1), end=" ")
        print(round(mysqrt(i, i), 11), end=(14 - len(str(round(mysqrt(i, i), 11)))) * " ")
        print(round(math.sqrt(i), 11), end=(14 - len(str(round(math.sqrt(i), 11)))) * " ")
        print(abs(math.sqrt(i) - mysqrt(i, i)))


if __name__ == "__main__":
    test_square_root()
    a = 12
    print(len(str(a)))
