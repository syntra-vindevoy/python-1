from sakamoto import day_of_the_week
from leapyear import is_leapyear

# This is a Python program that prints a calendar for the year 2022.
# It uses an import of the day_of_the_week algorithm that returns the day of the week as an int given any date according
# to the Gregorian calendar.
# It also uses an import of the is_leapyear function that returns a boolean

year = int(input("What year do you wish to print a calendar for? "))
days_heading = "MA DI WO DO VR ZA ZO"
month_heading = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER",
                 "NOVEMBER", "DECEMBER"]

# days_number is a list containing the number of days of the 12 months, in february 1 is added for leap years using
# the is_leapyear function

days_number = [31, 28 + 1 * is_leapyear(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print(f"This is a calendar for {year}")
for i in range(12):
    print(f"{month_heading[i]} {year}")
    print(days_heading)

    first_day_of_month = day_of_the_week(year, i + 1, 1)

    print(((day_of_the_week(year, i + 1, 1)) - 1) * "   ", end="")  # this adds the required blank spaces

    for j in range(1, days_number[i] + 1):
        print((j < 10) * "O" + str(j), end=" " + "\n" * (day_of_the_week(year, i + 1, j) == 7))

    print("\n")
