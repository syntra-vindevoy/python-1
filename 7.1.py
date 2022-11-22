import math
def frmt(text:str):
    return f"{text:.13f}"


def my_sqrt(a):
    x = a/2
    while True:
        y = (x + a / x) / 2
        if y == x:
            return y
            break
        x = y

def test_square_root(list_of_a):
    whitespace = " "
    line_1a = "a"
    line_1b = "mysqrt(a)"
    line_1c = "math.sqrt(a)"
    line_1d = "diff"

    line_2a = "-"
    line_2b = "---------"
    line_2c = "------------ "
    line_2d = "----"

    print(line_1a,line_1b,whitespace*5,line_1c,whitespace*2,line_1d)
    print(line_2a,line_2b,whitespace*5,line_2c,whitespace,line_2d)

    for a in list_of_a:

        column1 = a
        column2 = my_sqrt(a)
        column3 = math.sqrt(a)
        column4 = abs(my_sqrt(a)- math.sqrt(a))

        print(column1,frmt(column2),frmt(column3),column4)

test_square_root(range(1,10))
