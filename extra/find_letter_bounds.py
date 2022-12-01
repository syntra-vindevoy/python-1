""" Write a function that returns the lowest and highest ranking
letters in a given sentence. (char in [A-Za-z], and UPPER < LOWER)
jvdoorne, @Syntra, 01/12/2022
"""

import string


def find_letter_bounds(sentence: str) -> tuple:
    # Only accept comparisons between A-z
    lower_bound = chr(ord('z') + 1)
    upper_bound = chr(ord('A') - 1)

    # Begin with default low/high
    low, high = lower_bound, upper_bound
    for char in sentence:
        if char in string.ascii_letters:
            if char < low:
                low = char
            if char > high:
                high = char

    # Check if the found low/high in bounds of the default low/high
    return (low if low < lower_bound else None,
            high if high > upper_bound else None)


def find_letter_bounds_bis(sentence: str) -> tuple:
    # ~= Yves' solution
    low = high = None
    for char in sentence:
        if char in string.ascii_letters:
            if not any((low, high)):
                low = high = char
                continue
            if char < low:
                low = char
            if char > high:
                high = char
    return low, high


def find_letter_bounds_twoliner(sentence: str) -> tuple:
    s = sorted([x for x in sentence if x in string.ascii_letters])
    return (s[0], s[-1]) if s else (None, None)


def test(f) -> None:
    assert f(string.ascii_letters) == ('A', 'z')
    assert f('"Godverdomme!", zei de leraar.') == ('G', 'z')
    assert f('µ:=,; %£+/.?\n\t123') == (None, None)


if __name__ == '__main__':
    test(find_letter_bounds)
    test(find_letter_bounds_bis)
    test(find_letter_bounds_twoliner)
