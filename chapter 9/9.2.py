
def has_no_e(word: str) -> bool:
    if 'e' in word.lower():
        return False
    else:
        return True


with open("words.txt", "r") as input_file:
    lines = input_file.readlines()

for w in lines:
    if has_no_e(w):
        print(w)
