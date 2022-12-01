import math
import operator
from functools import reduce

monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]

def get_month_max_days(month, year):
    is_leap = month == 2 and ((year%100 == 0 and year%400 == 0) or (year%4 == 0 and year%100 != 0))
    return monthDays[month-1] + int(is_leap)

def sum_all_months_that_passed(toMonth, toYear):
    # reduce gaat alle items in de lijst de "operation.add" applien
    # 2e parameter in ons reduce is een lijst met alle max_dagen voor elk maand (met leap_year included)
    return reduce(operator.add, [get_month_max_days(month, toYear) for month in range(1, toMonth)])

def calculate_date(date):
    toYear, toMonth, toDay = (int(x) for x in date.split("-"))
    dayOfYear = sum_all_months_that_passed(toMonth, toYear) + toDay
    print(dayOfYear)
    print(math.ceil(dayOfYear/7))

calculate_date("1700-12-31")