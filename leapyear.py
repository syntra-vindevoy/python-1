def is_leapyear(x):
    if x % 4 != 0:
        return False
    return not ((x % 100 == 0) != (x % 400 == 0))


if __name__ == "__main__":

    #Assert testen
    assert is_leapyear(4)
    assert is_leapyear(8)
    assert not is_leapyear(9)
    assert not is_leapyear(100)
    assert is_leapyear(400)
    assert is_leapyear(2000)
    assert not is_leapyear(2001)
    assert not is_leapyear(2002)
    assert is_leapyear(2004)
    assert not is_leapyear(2100)
    assert is_leapyear(2400)
    assert not is_leapyear(1900)








