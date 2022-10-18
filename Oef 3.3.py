def do_twice(f):
    f()
    f()


def do_four(f):
    do_twice(f)
    do_twice(f)


def print_beam():
    print("+", 4 * "-", "+", 4*"-", "+")


def print_post():
    print("|", 4 * " ", "|", 4*" ", "|")


def print_half_grid():
    print_beam()
    do_four(print_post)


def print_grid():
    do_twice(print_half_grid)
    print_beam()


print_grid()


# print("+", 4* "-", "+", 4*"-", "+")
# print("+", end=' ')
