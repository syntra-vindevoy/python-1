""" Think Python Chapter 8, Exercise 8.5 (p.80)
I used two methods: one is short & sweet, but only works for
lowercase strings, the other is a more general function.
jvdoorne, @Syntra, 20/10/2022
"""


def rotate_lowercase(s: str, i: int) -> str:
    """ Encrypts / decrypts a lowercase string using a Caesar cypher,
    shifting the alphabet by a given integer. (Method 1)
    """
    key = "abcdefghijklmnopqrstuvwxyz"
    rot = key[i:] + key[:i]
    return "".join([rot[key.find(char)] for char in s])


def rotate_word(s: str, i: int) -> str:
    """ Encrypts / decrypts a given word using a Caesar cypher,
    shifting the alphabet by a given integer. (Method 2)
    """
    rot = ""
    for char in s:
        new_ord = ord(char) + i
        # Compensate for upper bound of alphabet
        if (char.isupper() and new_ord > ord('Z')) or \
                (char.islower() and new_ord > ord('z')):
            new_ord -= 26
        # Compensate for lower bound of alphabet
        if (char.isupper() and new_ord < ord('A')) or \
                (char.islower() and new_ord < ord('a')):
            new_ord += 26
        rot += chr(new_ord)
    return rot


if __name__ == '__main__':
    # Method 1
    assert rotate_lowercase("cheer", 7) == "jolly"
    assert rotate_lowercase("melon", -10) == "cubed"
    # Method 2
    assert rotate_word("cheer", 7) == "jolly"
    assert rotate_word("melon", -10) == "cubed"
