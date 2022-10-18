import turtle

from polygon import polygon


def circle(t, r):
    polygon(t, 360, r)


if __name__ == "__main__":
    bob = turtle.Turtle()

    circle(bob, 20)