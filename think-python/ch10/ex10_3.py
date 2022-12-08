""" Think Python Chapter 10, Exercise 10.3 (p.100)
jvdoorne, @Syntra, 08/12/2022
"""


def middle(l: list) -> list:
    return l[1:-1]


if __name__ == '__main__':
    assert middle([1, 2, 3, 4]) == [2, 3]
