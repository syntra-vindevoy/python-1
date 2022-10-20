def is_triangle(a: int, b: int, c: int):
    if a + b < c or a + c < b or b + c < a:
        print('No')
    else:
        print('yes')


def input_is_triangle():
    a = int(input('value for a:\n'))
    b = int(input('value for b:\n'))
    c = int(input('value for c:\n'))
    return is_triangle(a, b, c)


input_is_triangle()