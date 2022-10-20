def upper_line(s):
    print('+ ' + '- ' * (s - 1), end='')


def middle_line(s):
    print('| ' + '  ' * (s - 1), end='')


def mint_boxes(h, v, s):
    for height in range(h):
        for width in range(v):
            upper_line(s)
        print('+\n')
        for b in range(s - 1):
            for box in range(v):
                middle_line(s)
            print('|\n')
    for width in range(v):
        upper_line(s)
    print('+')


mint_boxes(2, 4, 5)

