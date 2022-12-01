def leapyear():

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
