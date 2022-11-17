def rotate_word(word, n):
    l = []
    for letter in word:
        if ord(letter) < 90:
            new_letter = chr((((n % 26) + ord(letter)) % 65) % 26 + 65)
            l.append(new_letter)
        else:
            new_letter = chr((((n % 26) + ord(letter.upper())) % 65) % 26 + 65).lower()
            l.append(new_letter)
    print("".join(l))


# for i in range(len(s)):
#    if ord(s[i]) > 96
#    s = s[:i] + chr(ord(s[i]) + n) + s[i + 1:]
#  print(s)


# rotate_word("bbb", -1)
print(ord("a"), ord("z"), ord("A"), ord("Z"))
print(chr(96), chr(123), chr(64))
print(((((5 % 26) + 90) % 65) % 26) + 65)

a = []
a.append("X")
a.append("Y")
print("".join(a))

rotate_word("aAa", 53)
