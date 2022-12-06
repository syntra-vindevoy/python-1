from dow_Tomohiko_Sakamoto import day_of_the_week
from leap_year import checkYear

# This program returns a calendar for the given year.
# Sakamoto gives the day of the week for a given date
# Leap_year returns true if the year is a leap_year


year = int(input("What year is the calendar? "))
month = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER",
         "DECEMBER"]
day = "Mo Tu We Th Fr Sa Su "
day_amount = [31, 28 + 1 * checkYear(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(12):
    print(month[i])
    print(day * 5)
    print(((day_of_the_week(year, i + 1, 1)) - 1) * "   ", end="")
    for x in range(1, day_amount[i] + 1):
        if x < 10:
            print("0" + str(x), end=" ")
        else:
            print(str(x), end=" ")
    print("\n")
