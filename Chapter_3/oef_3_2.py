from oef_3_1 import right_justify

def do_twice(f, value):
    f(value)
    f(value)
def print_spam(value):
    right_justify(value)

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_four(f, value):
    do_twice(f,value)
    do_twice(f,value)


if __name__ =="__main__": # dit zetten voor uitvoerbare code (testcode- zodat niet wordt uitgevoerd op een import)
    do_twice(print_spam,"toto")
    do_four(print_spam,"toto")




