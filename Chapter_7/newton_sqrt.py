def mysqrt(a, x):
    epsilon = 0.00000001
    while True:
        #print(x)
        y = (x + a / x) / 2

        if abs(y - x) < epsilon:
            break  # dead code

        x = y
    return y


if __name__ == "__main__":
    print(mysqrt(16, 7))
