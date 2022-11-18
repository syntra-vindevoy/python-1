# with open("words.txt", "r") as input.file:
#     lines = input.file.readlines()
#
# for line in lines:
#     words = line.strip()
#     if len(words) > 19:
#         print(words)



def characterCount():
    fin = open("words.txt")
    for line in fin:
        words = line.strip()
        if len(words) > 19:
            print(words)



characterCount()

