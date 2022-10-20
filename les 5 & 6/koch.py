import turtle
bob = turtle.Turtle()


def koch(t, length):
    t.fd(length // 3)
    t.lt(60)
    t.fd(length // 3)
    t.rt(120)
    t.fd(length // 3)
    t.lt(60)
    t.fd(length // 3)


def snowflake(t, length):
    koch(t, length)
    t.rt(120)
    koch(t, length)
    t.rt(120)
    koch(t, length)


snowflake(bob, 200)
turtle.mainloop()
