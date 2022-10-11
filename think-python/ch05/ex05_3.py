""" Think Python Chapter 5, Exercise 5.3 (p.48)
jvdoorne, @Syntra, 11/10/2022
"""


def is_triangle(a, b, c):
    print("Yes" if max(a, b, c) < sum(sorted([a, b, c])[:2]) else "No")


def let_user_check_triangle():
    is_triangle(int(input("Enter length of side 1: ")),
                int(input("Enter length of side 2: ")),
                int(input("Enter length of side 3: ")))


if __name__ == '__main__':
    let_user_check_triangle()
