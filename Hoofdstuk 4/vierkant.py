import turtle


def square(t):
    for i in range(4):
        t.fd (100)
        t.lt (90)

bob = turtle.Turtle()


if __name__ == "__main__":
    bob = turtle.Turtle()

    square(bob)

    turtle.mainloop()