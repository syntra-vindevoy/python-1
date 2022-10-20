"""
1. Write a function named check_fermat that takes four parameters—a, b, c and n—and
checks to see if Fermat’s theorem holds. If n is greater than 2 and
a
n + b
n = c
n
the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should
print, “No, that doesn’t work.
"""


def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        return print("Holy smokes, Fermat was wrong!")
    else:
        return print("No, that doesn’t work")


# def is_valid(x):
#     nog controleren of waarden groter zijn dan nul !!!


if __name__ == "__main__":
    print("Checking fermat's theorem, give a: ")
    a = int(input())
    print("Checking fermat's theorem, give b: ")
    b = int(input())
    print("Checking fermat's theorem, give c: ")
    c = int(input())
    print("Checking fermat's theorem, give n: ")
    n = int(input())
    result = check_fermat(a, b, c, n)
    print(result)
