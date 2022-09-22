

def print_grid(stripes):

    print('+', ('-' * stripes + '+') * stripes)

    for strip in range(stripes):

        for stripe in range(stripes):

            print("|", (" " * stripes + "|") * stripes)

        print('+', ('-' * stripes + '+') * stripes)


print_grid(5)
