""" Think Python Chapter 10, Exercise 10.4 (p.101)
jvdoorne, @Syntra, 08/12/2022
"""


def chop(l: list) -> None:
    global t
    t = l[1:-1]


if __name__ == '__main__':
    t = [1, 2, 3, 4]
    chop(t)
    assert t == [2, 3], t
