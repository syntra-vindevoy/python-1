""" Think Python Chapter 10, Exercise 10.2 (p.100)
jvdoorne, @Syntra, 08/12/2022
"""


def cumsum(l: list) -> list:
    s = l[:1]
    for i in range(1, len(l)):
        s.append((l[i] + s[i-1]))
    return s


if __name__ == '__main__':
    assert cumsum([1, 2, 3]) == [1, 3, 6]
