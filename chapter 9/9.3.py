def forbidden(word: str, letters: str) -> bool:

    for let in letters.lower():
        if let in word:
            return False

    return True


with open("words.txt", "r") as input_file:
    lines = input_file.readlines()

for w in lines:
    if forbidden(w, 'aeo'):
        print(w)
