a = 1


def toto():
    global a
    a = 2
    print(a)


toto()
print(a)


def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x


if __name__ == "__main__":
    for i in range(-5, 5):
        test = absolute_value(i)
        assert test >= 0, f"positive value expected, got: {test}"
