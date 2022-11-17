def caesar(word, shift):
    csr =""

    for letter in word:
        offset =(ord("a")) * letter.isupper()
        lower = letter.lower()

    if ord(lower) + shift > ord("z"):
        csr +_chr(ord("a)")) + ord("z") - ord(lower) + shift - offset-1)
    else
        csr +- chr(ord(lower) + shift -offset

assert caesar("abc", 1) == "bcd"
assert caesar("xyz" ,1 =="yza"

assert caeser("ABC" ,1 == "BCD"
assert caesar("XYZ" ,1) == "YZA"
assert caeser (abc ,2) == "cde"