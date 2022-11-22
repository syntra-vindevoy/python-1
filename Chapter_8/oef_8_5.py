def rotate_word(word, n):
    l = []
    for letter in word:
        if ord(letter) < 90:
            new_letter = chr((((n % 26) + ord(letter)) % 65) % 26 + 65)
            l.append(new_letter)
        else:
            new_letter = chr((((n % 26) + ord(letter.upper())) % 65) % 26 + 65).lower()
            l.append(new_letter)
    return"".join(l)



# rotate_word("bbb", -1)
#print(ord("a"), ord("z"), ord("A"), ord("Z"))
#print(chr(96), chr(123), chr(64))
#print(((((5 % 26) + 90) % 65) % 26) + 65)

if __name__ == "__main__":
    assert rotate_word("ABba", 2) == "CDdc"