def absolute_value(x):
    if x < 0:
        return -x

    else:
        return x


if __name__ == "__main__":
    def test1():
        for i in range(-5, 0):
            assert absolute_value(i) == -i, f"Value: {i}"

        for i in range(0, 6):
            assert absolute_value(i) == i, f"Value: {i}"




