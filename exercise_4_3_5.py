"""
5. Make a more general version of circle called arc that takes an additional parameter
angle, which determines what fraction of a circle to draw. angle is in units of degrees,
so when angle=360, arc should draw a complete circle.
"""
import turtle
import math


def arc(t, r, angle):
    n = r * 2 * math.pi
    for i in range(angle):
        t.fd(n / angle)
        t.lt(1)


bob = turtle.Turtle()
arc(bob, 100, 270)
turtle.mainloop()
