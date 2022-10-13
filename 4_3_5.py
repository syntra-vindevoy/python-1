import turtle
import math

length = 100
corner = 9
radiud = 90


def radius(t, r, d):
    # omtrek = 2*pi*r
    n = 2 * math.pi * r

    for i in range(360):
        t.fd(n / 360)
        t.lt(1)


# def polygon(t, l, n):
#     for _ in range(n):
#         t.fd(l)
#         t.lt(90 / n)


# if __name__ == "__main__":
#     bob = turtle.Turtle()
#     polygon(bob, length, corner)
#
#     turtle.mainloop()


if __name__ == "__main__":
    bob = turtle.Turtle()
    radius(bob, 100, radius())

    turtle.mainloop()