def absolute_value(x):
    assert isinstance (x, int) or type(x) == float

    if x < 0:
        return -x

    else:
        return x


if __name__ == "__main__":

    def test_int():
     for i in range(-1, 0):
        assert absolute_value(i) == -i, f"Value: {i}"

        for i in range(0, 6):
            assert absolute_value(i) == i, f"Value: {i}"
            f
    def test_float():
        assert absolute_value(2.5) == 2.5

        def test_string():
            ok = True

        try:
            assert absolute_value("a")

        except:
                ok = False

        assert not ok, "Does not work as expexted for "

    test_int()
    test_flaot()
    test_string()
