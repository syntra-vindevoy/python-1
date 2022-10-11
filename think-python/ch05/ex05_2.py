""" Think Python Chapter 5, Exercise 5.2 (p.48)
jvdoorne, @Syntra, 11/10/2022
"""


def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work")


def let_user_check_fermat():
    check_fermat(int(input("Enter value for a: ")),
                 int(input("Enter value for b: ")),
                 int(input("Enter value for c: ")),
                 int(input("Enter value for n: ")))


if __name__ == '__main__':
    let_user_check_fermat()
