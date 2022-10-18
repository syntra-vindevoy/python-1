import turtle
import math


def polygon(x, length, n, angle):
    for _ in range(angle):
        x.fd(length)
        x.lt(360 / n)


def arc(t, r, angle):
    polygon(t, (2 * r * math.pi) / 360, 360, angle)


if __name__ == "__main__":
    t = turtle.Turtle()
    bob = turtle.Turtle()
    arc(t, 50, 270)
    bob.lt(90)
    bob.fd(50)
    turtle.mainloop()
