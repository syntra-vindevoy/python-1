

def print_grid(h, b, stripes):

    print('+', ('-' * stripes + '+') * b)

    for strip in range(h):

        for stripe in range(stripes):

            print("|", (" " * stripes + "|") * b)

        print('+', ('-' * stripes + '+') * b)


if __name__ == '__main__':
    print_grid(6, 12, 5)
