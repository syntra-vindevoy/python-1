def print_calendar(month, year):
    months = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug",
              9: "Sept", 10: "Oct", 11: "Nov", 12: "Dec"}
    monthdays = {"Jan": 31, "Mar": 31, "Apr": 30, "May": 31, "Jun": 30, "Jul": 31, "Aug": 31,
                 "Sept": 30, "Oct": 31, "Nov": 30, "Dec": 31}
    month = int(month)
    year = int(year)

    # leapyear
    if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
        monthdays["Feb"] = 29
    else:
        monthdays["Feb"] = 28
    if 1 <= month <= 2:
        year -= 1
    if month < 3:
        a = month + 10
    else:
        a = month - 2
    b = 0  # day 1
    c = year % 100
    d = year // 100
    w = (13 * a - 1) // 5
    x = c // 4
    y = d // 4
    z = w + x + y + b + c - 2 * d
    r = z % 7
    r = (r + 7) % 7

    print(" " * 4 + months[month] + " " + str(year))
    print("Mo Tu We Th Fr Sa Su")

    for i in range(1, monthdays[months[month]] + 1):

        if i == 1:
            print((" " * 3) * r, end="")
        if i < 10:
            print("", i, end=" ")
        elif i >= 10:
            print(i, end=" ")
        if (i + r) % 7 == 0:
            print("\n", end="")


print_calendar(3, 2023)

#print("Time {:02}:{:02}".format(hours, minutes))