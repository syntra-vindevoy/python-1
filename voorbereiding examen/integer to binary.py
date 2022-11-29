

def make_binary():
    integer = 50
    binary = ""
    while integer != 0:
        if  integer % 2 == 1:
            binary += "1"

            integer = integer // 2
        elif integer % 2 == 0:
            binary += "0"
            integer = integer // 2


    print(binary[::-1])

make_binary()