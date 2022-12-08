""" Think Python Chapter 10, Exercise 10.7 (p.101)
jvdoorne, @Syntra, 08/12/2022
"""


def has_duplicates(l: list) -> bool:
    return len(l) != len(set(l))


if __name__ == '__main__':
    assert has_duplicates(list('tests'))
    assert not has_duplicates(list('tefal'))
