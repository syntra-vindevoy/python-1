from leapyear import is_leapyear


# This is a Python 3 program that returns what day of the year it is as an integer given any date according the
# gregorian calendar.
# It uses an import of the is_leapyear function that returns a boolean


#prompt = input("Please enter date as follows: dd/mm/yyyy \n")

#day = int(prompt[:2])
#month = int(prompt[3:5])
#year = int(prompt[6:])

def day_of_the_year(year, month, day):
    days_number = [31, 28 + 1 * is_leapyear(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    count = 0

    for i in range(month-1):
        count += days_number[i]

    count += day

    return count
