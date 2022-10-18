def absolute_value(x):
    assert isinstance(x, int) or type(x) == float

    if x < 0:
        return -x

    else:
        return x


if __name__ == "__main__":
    def test_int():
        for i in range(-1, 0):
            assert absolute_value(i) == -i, f"Value: {i}"

        for i in range(0, 2):
            assert absolute_value(i) == i, f"Value: {i}"

    def test_float():
        assert absolute_value(2.5) == 2.5

    def test_other():
        ok = True

        try:
            assert absolute_value("a")

        except:
            ok = False

        assert not ok, "Does not work as expected for strings"


        ok = True

        try:
            assert absolute_value(["b"])

        except:
            ok = False

        assert not ok, "Does not work as expected for lists"

    test_int()
    test_float()
    test_other()