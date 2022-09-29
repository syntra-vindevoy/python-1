""" Think Python Chapter 4, intermediate exercises (p.31)
jvdoorne, @Syntra, 29/09/2022
"""

import math
import turtle


def square(t: turtle.Turtle, length):
    for _ in range(4):
        t.fd(length)
        t.lt(90)


def polygon(t: turtle.Turtle, length, n):
    for _ in range(n):
        t.fd(length)
        t.lt(360 / n)


def circle(t: turtle.Turtle, r):
    circumference = 2 * r * math.pi
    polygon(t, circumference / 128, 128)


def arc(t: turtle.Turtle, r, angle):
    circumference = 2 * r * math.pi
    for _ in range(angle):
        t.fd(circumference / 360)
        t.lt(1)


if __name__ == '__main__':
    turt_reynolds = turtle.Turtle()
    square(turt_reynolds, 100)
    turt_reynolds.clear()
    polygon(turt_reynolds, 100, 6)
    turt_reynolds.clear()
    circle(turt_reynolds, 100)
    turt_reynolds.clear()
    arc(turt_reynolds, 100, 360)
    circle(turt_reynolds, 100)    # Should match `arc(t, 360)`
    turtle.mainloop()
