a = 1


def toto():
    # global a
    a = 2
    print(a)


if __name__ == "__main__":
    toto()
    print(a)
