""" Think Python Chapter 10, Exercise 10.5 (p.101)
jvdoorne, @Syntra, 08/12/2022
"""


def is_sorted(l: list) -> bool:
    return l == sorted(l)


if __name__ == '__main__':
    assert is_sorted([1, 4, 6, 14])
    assert not is_sorted([1, 3, 2, 5])
