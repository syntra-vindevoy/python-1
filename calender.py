def print_calendar(month, year):
    # Set up the dictionary
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
              9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    monthdays = {'January': 31, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31,
                 'September': 30, 'October': 31, 'November': 30, 'December': 31}
    month = int(month)
    year = int(year)
    # Calculate the leap year
    if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
        monthdays['February'] = 29
    else:
        monthdays['February'] = 28

    # Using Zeller's congruence
    # Change in year if month is January or February
    if 1 <= month <= 2:
        year -= 1
    # Switch months so that March becomes the first month of the year,
    # and January/ February become the 11th and 12th months respectively
    # Convert variables to algorithm variables (so a = month and b = day)
    if month < 3:
        a = month + 10
    else:
        a = month - 2
    b = 0  # The first day of the month
    c = year % 100
    d = year // 100
    # Compute starting weekdays with algorithm
    w = (13 * a - 1) // 5
    x = c // 4
    y = d // 4
    z = w + x + y + b + c - 2 * d
    r = z % 7
    r = (r + 7) % 7

    # Print the title
    space = ' '
    print(space * 4 + months[month] + space + str(year))
    #print("Su Mo Tu We Th Fr Sa")
    print("Mo Tu We Th Fr Sa Su")
    # Print out the calendar
    number = monthdays[months[month]]
    start_days = r
    for i in range(1, number + 1):
        if i == 1:
            print((space * 3) * start_days, end='')
        if i < 10:
            print('', i, end=' ')
        elif i >= 10:
            print(i, end=' ')
        if (i + start_days) % 7 == 0:
            print('\n', end='')


print_calendar('11', '2022')