""" Think Python Chapter 9, Exercise 9.1 (p.84)
jvdoorne, @Syntra, 17/11/2022
"""

from pathlib import Path

if __name__ == '__main__':
    with Path('../assets/words.txt').open() as f:
        word_list = f.read().split('\n')

    # Print woorden langer dan 20 chars
    for word in word_list:
        if len(word.replace(' ', '')) > 20:
            print(word)
