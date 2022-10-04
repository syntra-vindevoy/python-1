def do_twice(f):
    f()
    f()


def print_spam():
    print("spam")


if __name__ == "__main__":
    do_twice(print_spam)
