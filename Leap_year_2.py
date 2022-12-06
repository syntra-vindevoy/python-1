def leapyear_2():
    year = int(input("Enter Year: "))

    if year % 4 == 0 and year % 100 != 0:
        print("True")
    elif year % 100 == 0:
        print("False")
    elif year % 400 == 0:
        print("True")
    else:
        print("False")


leapyear()
