def any_lowercase1(s):  ## functie gecorrigeerd
    for c in s:
        if c.islower():
            return True
    return False


def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag


word = "HAHAHaAHH"
print(any_lowercase1(word))
# print(any_lowercase3(word))





