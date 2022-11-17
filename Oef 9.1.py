with open("words.txt", "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        line = line.replace(" ", "")
        if len(line) > 20:
            print(line)
#        else:
#            continue

