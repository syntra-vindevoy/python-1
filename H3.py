print("Oef 3.1")


def right_justify(txt):
    print((80 - int(len(txt)) * " " + txt))


right_justify("Monty")
right_justify("python")


print ("oef 3.2")

def do_twice (f):
    f()
    f()

def print_spam() :
    print('spam')


do_twice(print_spam)
