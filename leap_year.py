# Python program to check leap year or not
def checkYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# year = 2000
# if (checkYear(year)):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

assert checkYear(4)
assert not checkYear(1900)
assert checkYear(2000)
assert not checkYear(2001)
assert not checkYear(2002)

