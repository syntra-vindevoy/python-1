import turtle


def polygon(t, n, r):
    for _ in range(n):
        t.fd(r)
        t.lt(360 / n)


if __name__ == "__main__":
    bob = turtle.Turtle()

    polygon(bob, 8, 20)

    turtle.mainloop()