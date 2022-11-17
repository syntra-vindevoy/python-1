
def rotate_word(word, shift):
    """Uses Ceasar cypher to encrypt given word using given shift."""
    rotated_word = ''
    for letter in word:
        rotated_word += chr(ord(letter) + shift)
    return rotated_word

print(rotate_word('cheer', 7))
print(rotate_word('IBM', -1))
