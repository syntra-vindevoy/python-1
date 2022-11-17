# A Python 3 program to implement
# the Tomohiko Sakamoto Algorithm


# function to implement tomohiko
# sakamoto algorithm
def day_of_the_week(y, m, d):
    # array with leading number of days values
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]

    # if month is less than 3 reduce year by 1
    if m < 3:
        y = y - 1
    if ((y + y // 4 - y // 100 + y // 400 + t[m - 1] + d) % 7) == 0:
        return 7
    else:
        return (y + y // 4 - y // 100 + y // 400 + t[m - 1] + d) % 7


assert(day_of_the_week(1994, 12, 2) == 5)

assert(day_of_the_week(2022, 11, 14) == 1)
