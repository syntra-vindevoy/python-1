
with open("words.txt", "r") as input_file:
    lines = input_file.readlines()

    for word in lines:
        if len(word) > 20:
            print(word)
