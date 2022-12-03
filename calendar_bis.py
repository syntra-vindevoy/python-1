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
week = str((count - 1) // 7 + 1).rjust(2, " ")  # this renders the week number as a two character string

# days_number is a list containing the number of days in each of 12 months, in february 1 is added for leap years by
# multiplying the boolean output of is_leapyear with 1 and then adding it to 28

days_number = [31, 28 + 1 * is_leapyear(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print(f"THIS IS A CALENDAR FOR {year}")
for i in range(12):
    print(f"{month_heading[i]} {year}")
    print(days_heading)
    print(week, end=" ")
    first_day_of_month = day_of_the_week(year, i + 1, 1)

    print(((day_of_the_week(year, i + 1, 1)) - 1) * "   ", end="")  # this adds the required blank spaces

    for j in range(1, days_number[i] + 1):
        count += 1
        week = str((count - 1) // 7 + 1).rjust(2, " ")
        print((j < 10) * "O" + str(j), end=" " + "\n" * (day_of_the_week(year, i + 1, j) == 7))
        print(week * ((day_of_the_week(year, i + 1, j) == 7) and (j != days_number[i] )),
              end=" " * (day_of_the_week(year, i + 1, j) == 7))

    print("\n")
