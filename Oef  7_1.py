import math
i = 0

def initial_function(x, a):
    y = (x + a/x) / 2
    x = y
    return y


def precision_function(x, a):

    y = (x + a/x) / 2


def run():
    x = (int(input("x =")))
    a = (int(input("a =")))
    print(initial_function(x, a))

def test_square_root(a):
    for i in range(9):
        x = a + 1
        y = (x + a / x) / 2
        math_variable = math.sqrt(x)
        x = y
        i += 1
        a +=1

        print(str(a) + "   " + str(x) + "   "+ str(math_variable)+ "   " )



test_square_root((int(input("a ="))))
