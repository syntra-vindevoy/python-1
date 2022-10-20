"""
Exercise 3.3. Note: This exercise should be done using only the statements and other features we
have learned so far.
1. Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
Hint: to print more than one value on a line, you can print a comma-separated sequence of
values:
print('+', '-')
By default, print advances to the next line, but you can override that behavior and put a
space at the end, like this:
print('+', end=' ')
print('-')
"""


def linetype_1(s):
    """

    :param s: number of chars for each square
    :return: string for one square without right edge
    """
    return "+" + "-" * (s-1)


def linetype_1_end():
    """

    :return: string for right edge
    """
    return "+"


def linetype_2(s):
    """

    :param s: number of chars for each square
    :return: string for one square without right edge
    """
    return "|" + " " * (s - 1)


def linetype_2_end():
    """

    :return: string for right edge
    """
    return "|"


if __name__ == "__main__":
    horizontal = 7
    vertical = 2
    size = 5
    loop = 1

    while loop <= vertical:
        row = linetype_1(size) * horizontal + linetype_1_end()
        print(row)
        row = linetype_2(size) * horizontal + linetype_2_end()
        i = 1
        while i < size:
            print(row)
            i += 1
        loop += 1
    row = linetype_1(size) * horizontal + linetype_1_end()
    print(row)
