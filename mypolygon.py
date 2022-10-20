import turtle
import math


def polygon(t, n, lenght):
    for i in range(n):
        t.fd(lenght)
        t.lt(360 / n)


def square(t, lenght):
    for i in range(t):
        t.fd(lenght)
        t.lt(90)


def circl(t, r):
    n = r * 2 * math.pi
    for i in range(360):
        t.fd(n / 360)
        t.lt(1)

    bob = turtle.Turtle()

    circl(bob, 100)
