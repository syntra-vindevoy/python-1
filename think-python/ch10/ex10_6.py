""" Think Python Chapter 10, Exercise 10.6 (p.101)
jvdoorne, @Syntra, 08/12/2022
"""


def is_anagram(a, b) -> bool:
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    assert is_anagram('angel', 'glean')
    assert not is_anagram('angel', 'gleam')
