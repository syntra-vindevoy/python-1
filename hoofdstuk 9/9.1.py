def characterCount():
    with open("words.txt" , "r") as input_file:
        lines = input_file.readlines()
    for line in lines:
        words = line.strip()
        if len(words) > 19:
            print(words)
characterCount()

