""" Think Python Chapter 9, Exercise 9.2 (p.84)
jvdoorne, @Syntra, 17/11/2022
"""

from pathlib import Path


def no_e(word: str) -> bool:
    return "e" not in word


if __name__ == '__main__':
    with Path('../assets/words.txt').open() as f:
        word_list = f.read().split('\n')

    without_e = 0
    for item in word_list:
        if no_e(item):
            print(item)
            without_e += 1

    # Alternative
    print('\n'.join([x for x in word_list if no_e(x)]))

    # Statistics
    print(f"{without_e / without_e * 100:.2f}%")
