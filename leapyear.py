def leapyear(x):
    if x % 4 != 0:
        return False
    return not ((x % 100 == 0) != (x % 400 == 0))


if __name__ == "__main__":

    #Assert testen
    assert leapyear(4)
    assert leapyear(8)
    assert not leapyear(9)
    assert not leapyear(100)
    assert leapyear(400)
    assert leapyear(2000)
    assert not leapyear(2001)
    assert not leapyear(2002)
    assert leapyear(2004)
    assert not leapyear(2100)
    assert leapyear(2400)







