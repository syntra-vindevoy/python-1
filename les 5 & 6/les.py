a = 1


def toto():
    global a
    a = 2
    print(a)


toto()
print(a)
