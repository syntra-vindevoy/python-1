# List of tuples for Months and date ranges
calender = [('January', 31),
            ('Feburary', 28),
            ('March', 31),
            ('April', 30),
            ('May', 31),
            ('June', 30),
            ('July', 31),
            ('August', 31),
            ('September', 30),
            ('October', 31),
            ('November', 30),
            ('December', 31)]

week = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']


def make_calendar(year, start_day):
    """
    make_calendar(int, str) --> None
    """
    # Determine current starting position on calendar
    start_pos = week.index(start_day)

    # if True, adjust Feburary date range for leap year | 29 days
    if is_leap(year):
        calender[1] = ('Feburary', 29)

    for month, days in calender:
        # Print month title
        print('{0} {1}'.format(month, year).center(20, ' '))
        # Print Day headings
        print(''.join(['{0:<3}'.format(w) for w in week]))
        # Add spacing for non-zero starting position
        print('{0:<3}'.format('') * start_pos, end='')

        for day in range(1, days + 1):
            # Print day
            print('{0:<3}'.format(day), end='')
            start_pos += 1
            if start_pos == 7:
                # If start_pos == 7 (Sunday) start new line
                print()
                start_pos = 0  # Reset counter
        print('\n')


def is_leap(year):
    """Checks if year is a leap year"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


yr = int(input('Enter Year'))
strtday = input('Enter start day of the year Mo,Tu,We,Th,Fr,Sa,Su')
make_calendar(yr, strtday)