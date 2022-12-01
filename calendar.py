from sakamoto import day_of_the_week
from leapyear import is_leapyear

# This is a Python 3 program that prints a calendar for the year 2022.
# It uses an import of the day_of_the_week algorithm that returns the day of the week as an int given any date according
# to the Gregorian calendar.
# It also uses an import of the is_leapyear function that returns a boolean given a certain year as input

year = int(input("What year do you wish to print a calendar for? "))
days_heading = "wk MA DI WO DO VR ZA ZO"
month_heading = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER",
                 "NOVEMBER", "DECEMBER"]

count = day_of_the_week(year, 1, 1)
print(count)
week = (count // 7) + 1  # nog aanpassen
week_number = (week < 10) * " " + str(week)

# days_number is a list containing the number of days in each of 12 months, in february 1 is added for leap years by
# multiplying the boolean output of is_leapyear with 1 and then adding it to 28

days_number = [31, 28 + 1 * is_leapyear(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print(f"This is a calendar for {year}")
for i in range(12):
    print(f"{month_heading[i]} {year}")
    print(days_heading)
    print(week_number, end=" ")
    first_day_of_month = day_of_the_week(year, i + 1, 1)

    print(((day_of_the_week(year, i + 1, 1)) - 1) * "   ", end="")  # this adds the required blank spaces

    for j in range(1, days_number[i] + 1):
        print((j < 10) * "O" + str(j), end=" " + "\n" * (day_of_the_week(year, i + 1, j) == 7))

    print("\n")
