
def seek_letter():
    word = input("write a word: ")

    highest = "a"
    lowest = "z"

    for i in range(0, len(word)):
        #print((word[i]))
        if word[i] > highest:
            highest = word[i]

            #print(highest)
            #print(word[i])
            #print(type(highest))
            #print(type(word[i]))

        if word[i] < lowest:
            lowest = word[i]

            # print(lowest)
            # print(word[i])
            # print(type(lowest))
            # print(type(word[i]))

        else:
            continue
    print(highest)
    print(lowest)


seek_letter()