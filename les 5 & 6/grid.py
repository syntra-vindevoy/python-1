def do_twice(f):
    f()
    f()


def do_four(f):
    do_twice(f)
    do_twice(f)


def upper_line():
    print('+ - - - -', end=' ')


def middle_line():
    print('|        ', end=' ')


def beams():
    do_four(upper_line)
    print('+')


def post():
    do_four(middle_line)
    print('|')


def row():
    beams()
    do_four(post)


def grid():
    do_four(row)
    beams()


grid()
