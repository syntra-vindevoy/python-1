with open("words.txt", "r") as input.file:
    lines = input.file.readlines()

for line in lines:
    words = line.strip()
    if len(words) > 19:
        print(words)
