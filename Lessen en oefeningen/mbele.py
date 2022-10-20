def do_twice(f):
    f()
    f()


def do_four(f):
    do_twice(f)
    do_twice(f)


def print_beam():
    print('+ - - - -', end='')


def print_post():
    print('|        ', end=)
do_once(make_this)

