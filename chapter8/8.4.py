def rotate_word(word: str, number: int) -> str:
    new_word = str()

    for let in word:
        offset = (ord('a') - ord('A')) * let.isupper()
        if (ord(let.lower()) + number) > ord('z'):
            new_letter = chr(ord(let) + number - offset - 26)
        elif (ord(let.lower()) + number) < ord('a'):
            new_letter = chr(ord(let) + number - offset + 26)
        else:
            new_letter = chr(ord(let) + number - offset)
        new_word += new_letter

    return new_word


print(rotate_word('cubed', 10))

