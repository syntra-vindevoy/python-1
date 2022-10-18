import turtle


def koch(t, x):
    if x < 10:
        t.fd(x)

    else:
        koch(t, x / 10)
        t.lt(60)
        koch(t, x / 10)
        t.rt(120)
        koch(t, x / 10)
        t.lt(60)
        koch(t, x / 10)


def snowflake(t, x):
    for i in range(3):
        koch(t, x)
        t.rt(120)


if __name__ == "__main__":
    import turtle

    bob = turtle.Turtle()
    #koch(bob, 1000)
    snowflake(bob, 1000)


    turtle.mainloop()
