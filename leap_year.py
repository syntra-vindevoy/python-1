j = int(input("enter jaar: "))
def leapyear():

    if j % 4 == 0 and j % 100 != 0:
        print("ja")
    elif j % 100 == 0:
        print("neen")
    elif j % 400 == 0:
        print("ja")
    else:
        print("neen")


if __name__ == "__main__":
    leapyear()

