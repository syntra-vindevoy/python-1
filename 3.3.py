def do_twice(f: object) -> object:
    f()
    f()

def do_four(f):
    do_twice('t')
    do_twice('t')

def print_beam():
    print('+----', end=' ')

def print_post():
    print('|    ', end=' ')

def print_beams():
    print_beam()
    do_four(print_post)

def print_posts():
    do_twice(print_post())
    print('|')

def print_row():
    print_beams()
    do_four(print_posts())

def print_grid():
    do_twice(print_row())
    print_beams()
    
print(print_grid())