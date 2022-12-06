


def calandar(m, j):
    maanden = {1: "jan", 2: "feb", 3: "maart", 4: "apr", 5: "mei", 6: "jun", 7: "jul", 8: "aug", 9: "sep", 10: "okt", 11: "nov", 12: "dec"}
    dagen_maand = {"jan": 31, "maart": 31, "apr": 30, "mei": 31, "jun": 30, "jul": 31, "aug": 31, "sept": 30, "okt": 31, "nov": 30, "dec": 31}

    m = int(m)
    j = int(j)

    if ly == "true":
        dagen_maand["feb"] = 29
    else:
        dagen_maand["feb"] = 28
    if 1 <= m <= 2:
        j -= 1
    if m < 3:
        a = m + 10
    else:
        a = m - 2
    b = 0
    c = j % 100
    d = j // 100
    w = (13 * a - 1) // 5
    x = c // 4
    y = d // 4
    z = w + x + y + b + c - 2 * d
    r = z % 7
    r = (r + 7) % 7



    print("Ma Di Wo Do Vr Za Zo")

    for i in range(1, dagen_maand[maanden[m]] + 1):

        if i == 1:
            print((" " * 3) * r, end="")
        if i < 10:
            print("", i, end=" ")
        elif i >= 10:
            print(i, end=" ")
        if (i + r) % 7 == 0:
            print("\n", end="")


calandar(2, 2024)


