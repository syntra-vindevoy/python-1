def check_fermat(a, b, c, n):
    if n > 2 and a ** n + b ** n == c ** n:
        print(f'Holy smokes, Fermat was wrong!')
    else:
        print(f"No, that doesn't work.")


def input_check_fermat():
    a = int(input('value for a:'))
    b = int(input('value for b:'))
    c = int(input('value for c:'))
    n = int(input('value for n:'))
    return check_fermat(a, b, c, n)
