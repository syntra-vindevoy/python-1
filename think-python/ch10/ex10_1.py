""" Think Python Chapter 10, Exercise 10.1 (p.100)
jvdoorne, @Syntra, 08/12/2022
"""


def nested_sum(l: list) -> int:
    s = 0
    for sub in l:
        s += sum(sub)
    return s


def nested_sum_oneliner(l: list) -> int:
    return sum([sum(x) for x in l])


if __name__ == '__main__':
    assert nested_sum([[1, 2], [3], [4, 5, 6]]) == 21
    assert nested_sum_oneliner([[1, 2], [3], [4, 5, 6]]) == 21
