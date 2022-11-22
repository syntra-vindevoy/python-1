""" Checks Tomohiko Sakomoto's algorithm for finding the day of the week.
https://www.geeksforgeeks.org/tomohiko-sakamotos-algorithm-finding-day-week
(Added us_format parameter, for ISO/US compatibility)
jvdoorne, @Syntra, 17/11/2022
"""


def day_of_the_week(y, m, d, us_format=False):
    # array with leading number of days values
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    # if month is less than 3 reduce year by 1
    if m < 3:
        y = y - 1
    return (y + y // 4 - y // 100 + y // 400 + t[m - 1] + d) % 7 + us_format


if __name__ == '__main__':

    # ISO format
    assert day_of_the_week(1, 1, 1) == 1
    assert day_of_the_week(2012, 12, 21) == 5
    assert day_of_the_week(2022, 11, 17) == 4

    # US format
    assert day_of_the_week(1, 1, 1, True) == 2
    assert day_of_the_week(2012, 12, 21, True) == 6
    assert day_of_the_week(2022, 11, 17, True) == 5
