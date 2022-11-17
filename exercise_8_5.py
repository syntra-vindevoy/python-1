"""
Exercise 8.5. A Caesar cypher is a weak form of encryption that involves “rotating” each letter by
a fixed number of places. To rotate a letter means to shift it through the alphabet, wrapping around
to the beginning if necessary, so ’A’ rotated by 3 is ’D’ and ’Z’ rotated by 1 is ’A’.
To rotate a word, rotate each letter by the same amount. For example, “cheer” rotated by 7 is “jolly”
and “melon” rotated by -10 is “cubed”. In the movie 2001: A Space Odyssey, the ship computer
is called HAL, which is IBM rotated by -1.

Write a function called rotate_word that takes a string and an integer as parameters, and returns
a new string that contains the letters from the original string rotated by the given amount.

You might want to use the built-in function ord, which converts a character to a numeric code, and
chr, which converts numeric codes to characters. Letters of the alphabet are encoded in alphabetical
order, so for example:
 ord('c') - ord('a')
2
Because 'c' is the two-eth letter of the alphabet. But beware: the numeric codes for upper case
letters are different.
Potentially offensive jokes on the Internet are sometimes encoded in ROT13, which is a Caesar
cypher with rotation 13. If you are not easily offended, find and decode some of them. Solution:
http: // thinkpython2. com/ code/ rotate. py .
a = 97
z = 122
A = 65
Z = 90

"""
word = "ABC"


def rotate_word(word: str, x: int):
    temp = ''
    for letter in word:
        test = ord(letter)
        if 96 < test < 123:
            nieuw = test + x
            if nieuw < 97:
                t = 97 - nieuw
                temp += chr(123 - t)
            elif nieuw > 122:
                t = nieuw - 122
                temp += chr(96 + t)
            else:
                temp += chr(ord(letter) + x)
        if 64 < test < 91:
            nieuw = test + x
            if nieuw < 65:
                t = 65 - nieuw
                temp += chr(91 - t)
            elif nieuw > 90:
                t = nieuw - 90
                temp += chr(64 + t)
            else:
                temp += chr(ord(letter) + x)
    return temp

print(rotate_word(word, 10))

assert rotate_word("abc", 1) == "bcd"
assert rotate_word("xyz", 1) == "yza"
assert rotate_word("ABC", 1) == "BCD"
assert rotate_word("XYZ", 1) == "YZA"
assert rotate_word("abc", 2) == "cde"
assert rotate_word("aBcE", 2) == "cDeG"
