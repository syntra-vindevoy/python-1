def do_twice(f, value):
    f(value)
    f(value)


def print_spam():
    print('spam')


def print_twice(arg):
    print(arg)
    print(arg)


def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)


do_twice(print, 'spam')
do_four(print, 'spam')

