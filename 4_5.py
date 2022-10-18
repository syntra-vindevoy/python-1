import math
import turtle


def arc(t, r, d):
    # omtrek = 2*pi*r

    n = 2 * math.pi * r

    for i in range(d):
        t.fd(n/360)
        t.lt(1)


def circle(t, r):
    arc(t, r, 360)


def __polygon(t, l, n):
    for i in range(n):
        t.fd(l)
        t.lt(360 / n)


def square(t, l):
    __polygon(t, l, 4)


if __name__ == "__main__":
    bob = turtle.Turtle()

    arc(bob, radius, 90)

    turtle.mainloop()
