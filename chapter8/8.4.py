def rotate_word(word: str, number: int) -> str:
    new_word = str()

    def return_ord(letter, n):
        if ord(letter.lower()) + n < 65:
            return ord(letter) + n + 26
        else:
            return ord(letter) + n

    for let in word:

        new_letter = chr(return_ord(let, number))
        new_word += new_letter

    return new_word


print(rotate_word('IBM', -1))


