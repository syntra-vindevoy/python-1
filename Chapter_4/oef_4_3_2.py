import turtle


def square(x, length):
    for _ in range(4):
        x.fd(length)
        x.lt(90)


if __name__ == "__main__":
    t = turtle.Turtle()

    square(t, 200)
    turtle.mainloop()
