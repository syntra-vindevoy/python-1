days_in_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def _is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
def dd_mm_yy(date):
    list_day_month_year = date.split("-")
    day = int(list_day_month_year[0])
    month = int(list_day_month_year[1])
    year = int(list_day_month_year[2])

    counter = 0
    total_days_excluding_current_month = 0
    while counter != month - 1:
        total_days_excluding_current_month += amount_of_days_in_mm_yy(counter,year)
        counter += 1
    total_days = total_days_excluding_current_month + day
    return total_days
def amount_of_days_in_mm_yy(month,year):
    _days = days_in_year[month]
    if month == 1 and _is_leap(year):
        _days += 1
    return _days
def week_number(date):
    test = dd_mm_yy(date) // 7
    return  test
date_to_test = input("Type a date in format: DD-MM-YYYY")

print(f" Day number: {dd_mm_yy(date_to_test)}\n Weeknumber: {week_number(date_to_test)}")

