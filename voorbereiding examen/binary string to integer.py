#REDENEER FOUT IN REKENEN BINAIR


binary_string = "110010"


def convert_to_binary():
    binary = 0
    exponent = 0
    x = binary_string[::-1]

    #print(x)
    for i in range(0, len(x)):
        print(int(x[i]))
        print(int(exponent))
        exponent += 1
        binary += int(x[i])**int(exponent)
        #print(binary)
    print(binary)


convert_to_binary()

#assert convert_to_binary()
#assert 11 = 3