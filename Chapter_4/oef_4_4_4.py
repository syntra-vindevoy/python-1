import turtle
import math


def polygon(x, length, n):
    for _ in range(n):
        x.fd(length)
        x.lt(360 / n)


def circle(t, r):
    polygon(x=t, length = (2 * r * math.pi) / 360, n=360)


if __name__ == "__main__":
    t = turtle.Turtle()
    bob = turtle.Turtle()  # extra turtle to draw the radius
    circle(t, 200)
    bob.lt(90)
    bob.fd(200)

    turtle.mainloop()
