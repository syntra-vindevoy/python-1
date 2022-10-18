# slechte codes met test waardoor we zien dat het niet werkt.
def absolute_value(x):
    if x < 0:
        return -x
    if x > 0:
        return x

if __name__ == "__main__":
    def test():
        for i in range(-5, 0):
            assert absolute_value(i) == -i, f"value: {i}"
            # f"value: {i}"  --> om naar een string te formateren
        for i in range(0, 6):
            assert absolute_value(i) == i, f"value: {i}"

    def test_float():
        assert absolute_value(2.5) == 2.5
    def test_string():
    ok = true

    try:
        assert absolute_value("a")
    except
        ok = false
    assert not ok, "does not work as expected for lists"

#assert: value moet true zijn, ideaal om te debuggen

test()
test_float()
test_string()
test_int() #eigenlijk ook testen, hier niet gedaan
