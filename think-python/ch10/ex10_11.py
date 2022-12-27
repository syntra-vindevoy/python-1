""" Think Python Chapter 10, Exercise 10.11 (p.101)
jvdoorne, @Home, 27/12/2022
"""

from ex10_10 import in_bisect


def reverse_pairs(collection: list) -> int:
    reverse = [x[::-1] for x in collection]
    return [in_bisect(word, collection) for word in reverse].count(True)


if __name__ == '__main__':

    with open('../assets/words.txt') as f:
        words = sorted([x.strip().lower() for x in f.readlines()])

    assert reverse_pairs(words) == 885
