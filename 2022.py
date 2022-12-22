year = int(input("What year do you wish to print a calendar for? "))
def isleapyear(year):
    """Using the algorithm provided in the worksheet, this function determines whether any given year is a leap year
    or not """
    if 0 == year % 400:
        return True
    elif 0 == year % 100:
        return False
    elif 0 == year % 4:
        return True
    else:
        return False


def days_in_month(month, year2):
    """
    *determining the length of any given month,
    *the year is given as a parameter as well because in a leap year, February is a day longer
    What this function does,
    *is checking in which one of the two lists the month is in and returning 31 or 30,
    unless of course the given month is February in which case
    *is checking whether the given year is a leap year or not and then returns 29 or 28 respectively. """
    list1 = [1, 3, 5, 7, 8, 10, 12]
    list2 = [4, 6, 9, 11]
    if month != 2:
        for i in list1:
            if month == i:
                return 31
        for i in list2:
            if month == i:
                return 30
    elif isleapyear(year2):
        return 29
    else:
        return 28


def week_day(day, month, year):
    # array with leading number of days values
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]

    # if month is less than 3 reduce year by 1
    if month < 3:
        year = year - 1

    a = (year + year // 4 - year // 100 + year // 400 + t[month - 1] + day) % 7
    if a % 7 == 0:
        return 7
    else:
        return a


def name_day(b):
    """returns the name of the day of the week, which is the parameter b"""
    # list=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[b - 1]


def month_name(m):
    """ returns the name of the month which is the parameter m"""
    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
             "November", "December"]
    return month[m - 1]


def calendar(year):
    """this function checks
    *for every day of every month, whether or not it is the first day of the month,
    *the last day of the week, the last day of the month,
    * or the last day of the week and the first day of the month
    *or the last day of the month and the last day of the week as week,
    to then place it appropriately in the printed line"""
    kalenderweek = 0
    print(f"THIS IS A CALENDAR FOR {year}")
    for i in range(1, 13):
        string = "        " + month_name(i) + " " + str(year)
        # week_names= "W  " + "Zo " + "Ma  " + "Di  " + "Woe  " + "Do  " + "Fr  " + "Sa  "
        week_names = "W  " + "Ma  " + "Di  " + "Woe  " + "Do  " + "Fr  " + "Sa  " + "Zo "
        print(string + "\n" + week_names)
        teller = 0
        firstday = week_day(1, i, year)
        n = 1
        for j in range(1, days_in_month(i, year) + 1):
            if teller == 0:
                print('%02d' % kalenderweek, end=" ")
                if j == 1:
                    while n < firstday:
                        n += 1
                        print("  ", end="  ")
                        teller += 1
                    if firstday == 7:
                        print('%2d' % j, end="  ")
                        print("\n")
                    else:
                        print('%2d' % j, end="  ")
                else:
                    print('%2d' % j, end="  ")
                teller += 1
            elif teller != 6:
                print('%2d' % j, end="  ")
                teller += 1
            if j == days_in_month(i, year) and week_day(j, i, year) != 7:
                print("\n ")
            if week_day(j, i, year) == 7:
                if j > 1 and j != days_in_month(i, year):
                    print('%2d' % j, end="  ")
                    kalenderweek += 1
                    teller = 0
                    print("\n")
                elif j == days_in_month(i, year):
                    print('%2d' % j, end="  ")
                    kalenderweek += 1
                    print("\n")
                elif j == 1:
                    kalenderweek += 1
                    teller = 0


calendar(year)
