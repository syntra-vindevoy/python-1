import turtle


def polygon(t, n):

    for _ in range(4):
         t.fd(1000)
         t.lt(360 / n)


if __name__ == "__main__":
    bob = turtle.Turtle()

    polygon(bob, 360)

turtle.mainloop()
