def do_twice(f, g):
    f(g)
    f(g)

def print_spam(s):
    print(s)

do_twice(print_spam, 'spam')