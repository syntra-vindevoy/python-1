def leapyear():
    j = int(input("enter jaar: "))

    if j % 4 == 0 and j % 100 != 0:
        print ("true")
    elif j % 100 == 0:
        print ("false")
    elif j % 400 == 0:
        print ("true")
    else:
        print ("false")


leapyear()