
def is_leapyear(year):
    if year % 4 != 0:
        return False

    if year % 100 == 0 and year % 400 != 0:
        return False

    return True


assert is_leapyear(2000)
assert not is_leapyear(2001)
assert not is_leapyear(2002)
assert not is_leapyear(2003)
assert is_leapyear(2004)
assert not is_leapyear(2100)
assert not is_leapyear(2200)
assert is_leapyear(2400)
