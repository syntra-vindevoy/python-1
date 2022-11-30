def print_calendar(month, year):
    months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
              9: "September", 10: "October", 11: "November", 12: "December"}
    monthdays = {"January": 31, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31,
                 "September": 30, "October": 31, "November": 30, "December": 31}
    month = int(month)
    year = int(year)
    # leapyear
    if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
        monthdays["February"] = 29
    else:
        monthdays["February"] = 28
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

    # title
    space = ' '
    print(space * 4 + months[month] + space + str(year))
    print("Mo Tu We Th Fr Sa Su")
    # the calendar
    number = monthdays[months[month]]
    start_days = r
    for i in range(1, number + 1):
        if i == 1:
            print((space * 3) * start_days, end="")
        if i < 10:
            print("", i, end=" ")
        elif i >= 10:
            print(i, end=' ')
        if (i + start_days) % 7 == 0:
            print("\n", end="")


print_calendar("1", "2023")
