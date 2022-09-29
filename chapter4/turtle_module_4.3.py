

import turtle


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)


kris = turtle.Turtle()



import math

"""
Write a function called circle that takes a turtle, t, and radius, r, as parameters and
that draws an approximate circle by calling polygon with an appropriate length and
number of sides. Test your function with a range of values of r.
Hint: figure out the circumference of the circle and make sure that length * n =
circumference.
"""

"""Make a more general version of circle called arc that takes an additional parameter
angle, which determines what fraction of a circle to draw. angle is in units of degrees,
so when angle=360, arc should draw a complete circle."""


def circle_arc(t, radius, angle): # angle = 360 gives a circle

    n = 360

    length = (2 * math.pi * radius) / n

    for i in range(angle):
        t.fd(length)
        t.lt(360/n)


if __name__ == '__main__':

    kris = turtle.Turtle()
    square(kris, 100)
    polygon(kris, 100, 10)
    circle_arc(kris, 100, 90)


