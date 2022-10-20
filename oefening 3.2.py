def do_twice(f) -> object:
    f()
    f()
    f()
    f()

def print_spam():
        print('spam')

#if __name__ == "__main__": #gebruik dit om bij import de functie uit te sluiten

do_twice(print_spam)