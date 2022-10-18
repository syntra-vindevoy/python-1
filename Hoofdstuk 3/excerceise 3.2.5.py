# Define a new function called do_four that takes a function object
# and a value and calls the function four times, passing the value as
# a parameter. There should be only two statements in the body of this
# function, not four.

arg = 'spam'
def do_twice(f, arg):
    f(arg)
    f(arg)

def print_twice(arg):
    print(arg)
    print(arg)

def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)

do_four(print_twice, arg)