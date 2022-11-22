with open("words.txt", "r") as input_file:
    lines = input_file.readlines()

for line in lines:
    word = line.strip()
    if len(word) > 20:
        print(word)



