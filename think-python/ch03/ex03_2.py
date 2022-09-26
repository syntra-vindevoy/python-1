""" Think Python Chapter 3, Exercise 3.2 (p.27)
jvdoorne, @Home, 26/09/2022
"""


def do_twice(f, arg):
    f(arg)
    f(arg)


def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)


def print_twice(s):
    print(s)
    print(s)


if __name__ == '__main__':
    do_four(print_twice, "spam")
