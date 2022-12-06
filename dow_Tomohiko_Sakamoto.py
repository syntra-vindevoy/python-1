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

    x = (y + y // 4 - y // 100 + y // 400 + t[m - 1] + d) % 7

    # sunday is 7 instead of 0

    if x % 7 == 0:
        return 7
    else:
        return x


# Driver Code
# day = 13
# month = 7
# year = 2017

# print(day_of_the_week(year, month, day))

if __name__ == "__main__":
    assert day_of_the_week(2022, 11, 17) == 4
    assert day_of_the_week(2022, 11, 16) == 3
    assert day_of_the_week(1983, 3, 23) == 3
    assert day_of_the_week(2022, 12, 4) == 0

    print(day_of_the_week(2022, 11, 17))
    print(day_of_the_week(2022, 11, 16))
    print(day_of_the_week(1983, 3, 23))
    print(day_of_the_week(2022, 1, 1))
    print(day_of_the_week(2022, 12, 4))
# This code is contributed by Nikita Tiwari.
