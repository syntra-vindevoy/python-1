def leapyear():
    j = int(input("enter jaar: "))

    if j % 4 == 0 and j % 100 != 0:
        return ("true")
    elif j % 100 == 0:
        return ("false")
    elif j % 400 == 0:
        return ("true")
    else:
        return ("false")


leapyear()