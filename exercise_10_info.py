"""maak volgende functie die bepaalde indexen verwijderd, verplicht delete gebruiken"""


def delete_by_index2(word, index):
    return "".join([word[j] for j in range(len(word)) if j not in index])


def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1


def delete_by_index(word, index):
    lst = []
    for item in word:
        lst.append(item)
    rev_index = index[::-1]
    result = lst
    for x in rev_index:
        result.pop(x)
    result = listToString(result)
    print(result)

delete_by_index("Vindevogel", [1, 4, 9])


# resultaat ==> "Vndvoge"



# def only_upper(w):
#     return "".join([l for l in w if l.isupper()])