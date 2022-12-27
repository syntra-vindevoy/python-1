""" Think Python Chapter 10, Exercise 10.10 (p.101)
jvdoorne, @Home, 27/12/2022
"""


def in_bisect(word: str, collection: list) -> bool:
    low, high = 0, len(collection) - 1
    while low <= high:
        pivot = low + (high - low) // 2
        guess = collection[pivot]
        if guess == word:
            return True
        elif guess < word:
            low = pivot + 1
        else:
            high = pivot - 1
    return False


if __name__ == '__main__':

    with open('../assets/words.txt') as f:
        words = sorted([x.strip().lower() for x in f.readlines()])

    assert in_bisect('aa', words)
    assert in_bisect('bisect', words)
    assert in_bisect('zymurgy', words)
    assert not in_bisect('syntra', words)       # Not in words.txt
